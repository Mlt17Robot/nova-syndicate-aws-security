#!/usr/bin/env python3
import boto3
from botocore.exceptions import ClientError

REGION = "eu-west-3"

RDS_INSTANCE_ID = "nova-syndicate-postgresql"
ASG_NAME = "NovaSyndicate-App-ASG"
BACKUP_VAULT_NAME = "NovaSyndicate-Backup-Vault"


def print_header():
    print("=" * 48)
    print("NOVA SYNDICATE HEALTH CHECK")
    print("=" * 48)


def ok(message):
    print(f"[OK] {message}")


def warning(message):
    print(f"[WARNING] {message}")


def critical(message):
    print(f"[CRITICAL] {message}")


def check_rds():
    print("\nRDS:")
    rds = boto3.client("rds", region_name=REGION)

    try:
        response = rds.describe_db_instances(
            DBInstanceIdentifier=RDS_INSTANCE_ID
        )
        db = response["DBInstances"][0]
        status = db["DBInstanceStatus"]

        if status == "available":
            ok(f"RDS instance '{RDS_INSTANCE_ID}' is available")
            return True
        else:
            warning(f"RDS instance status is '{status}'")
            return False

    except ClientError as e:
        critical(f"Unable to check RDS: {e}")
        return False


def check_asg():
    print("\nAuto Scaling Group:")
    autoscaling = boto3.client("autoscaling", region_name=REGION)

    try:
        response = autoscaling.describe_auto_scaling_groups(
            AutoScalingGroupNames=[ASG_NAME]
        )

        if not response["AutoScalingGroups"]:
            critical(f"ASG '{ASG_NAME}' not found")
            return False

        asg = response["AutoScalingGroups"][0]
        desired = asg["DesiredCapacity"]
        min_size = asg["MinSize"]
        max_size = asg["MaxSize"]
        instances = asg["Instances"]

        healthy_instances = [
            i for i in instances if i["HealthStatus"] == "Healthy"
        ]

        print(f"Desired Capacity: {desired}")
        print(f"Min Size: {min_size}")
        print(f"Max Size: {max_size}")
        print(f"Healthy Instances: {len(healthy_instances)}")

        if desired >= 1 and len(healthy_instances) >= 1:
            ok(f"ASG '{ASG_NAME}' has healthy instances")
            return True
        elif desired == 0:
            warning("ASG desired capacity is 0. Environment may be stopped intentionally.")
            return True
        else:
            critical("ASG has no healthy instances")
            return False

    except ClientError as e:
        critical(f"Unable to check ASG: {e}")
        return False


def check_alb_targets():
    print("\nApplication Load Balancer:")
    elbv2 = boto3.client("elbv2", region_name=REGION)

    try:
        target_groups = elbv2.describe_target_groups()["TargetGroups"]

        if not target_groups:
            warning("No target group found")
            return False

        global_status = True

        for tg in target_groups:
            tg_name = tg["TargetGroupName"]
            tg_arn = tg["TargetGroupArn"]

            health = elbv2.describe_target_health(
                TargetGroupArn=tg_arn
            )

            targets = health["TargetHealthDescriptions"]
            healthy_targets = [
                t for t in targets if t["TargetHealth"]["State"] == "healthy"
            ]

            print(f"Target Group: {tg_name}")
            print(f"Healthy Targets: {len(healthy_targets)} / {len(targets)}")

            if len(targets) == 0:
                warning(f"No registered targets in target group '{tg_name}'")
                global_status = False
            elif len(healthy_targets) == len(targets):
                ok(f"All targets healthy in '{tg_name}'")
            else:
                critical(f"Some targets are unhealthy in '{tg_name}'")
                global_status = False

        return global_status

    except ClientError as e:
        critical(f"Unable to check ALB targets: {e}")
        return False


def check_cloudwatch_alarms():
    print("\nCloudWatch:")
    cloudwatch = boto3.client("cloudwatch", region_name=REGION)

    try:
        response = cloudwatch.describe_alarms(
            StateValue="ALARM"
        )

        alarms = response["MetricAlarms"]

        if not alarms:
            ok("No active CloudWatch alarms")
            return True

        for alarm in alarms:
            warning(f"Alarm active: {alarm['AlarmName']}")

        return False

    except ClientError as e:
        critical(f"Unable to check CloudWatch alarms: {e}")
        return False


def check_backup_jobs():
    print("\nAWS Backup:")
    backup = boto3.client("backup", region_name=REGION)

    try:
        response = backup.list_backup_jobs(
            ByBackupVaultName=BACKUP_VAULT_NAME,
            MaxResults=10
        )

        jobs = response.get("BackupJobs", [])

        if not jobs:
            warning("No backup jobs found")
            return False

        latest_job = sorted(
            jobs,
            key=lambda x: x["CreationDate"],
            reverse=True
        )[0]

        state = latest_job["State"]
        resource = latest_job.get("ResourceArn", "Unknown resource")

        print(f"Latest Backup State: {state}")
        print(f"Resource: {resource}")

        if state == "COMPLETED":
            ok("Latest backup completed successfully")
            return True
        else:
            warning(f"Latest backup state is '{state}'")
            return False

    except ClientError as e:
        critical(f"Unable to check AWS Backup: {e}")
        return False


def main():
    print_header()

    results = {
        "RDS": check_rds(),
        "ASG": check_asg(),
        "ALB": check_alb_targets(),
        "CloudWatch": check_cloudwatch_alarms(),
        "Backup": check_backup_jobs(),
    }

    print("\n" + "-" * 48)

    if all(results.values()):
        print("GLOBAL STATUS: HEALTHY")
    else:
        print("GLOBAL STATUS: WARNING / ACTION REQUIRED")

    print("-" * 48)


if __name__ == "__main__":
    main()