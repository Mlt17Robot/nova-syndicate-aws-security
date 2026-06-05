# Nova Syndicate Operational Runbook

## Version Information

| Field       | Value               |
| ----------- | ------------------- |
| Document    | Operational Runbook |
| Version     | 1.0                 |
| Environment | Production          |
| Status      | Approved            |

---

# 1. Purpose

This runbook provides operational procedures for managing, monitoring, starting, stopping, and troubleshooting the Nova Syndicate AWS environment.

---

# 2. Environment Overview

## Core Components

* Application Load Balancer (ALB)
* Auto Scaling Group (ASG)
* Amazon EC2
* Amazon RDS PostgreSQL
* AWS Backup
* CloudWatch
* CloudTrail
* GuardDuty
* Security Hub
* Systems Manager

---

# 3. Start Environment Procedure

## Step 1 – Start Database

```bash
aws rds start-db-instance \
--db-instance-identifier nova-syndicate-postgresql \
--region eu-west-3
```

Verify:

```bash
aws rds describe-db-instances \
--db-instance-identifier nova-syndicate-postgresql \
--query "DBInstances[0].DBInstanceStatus"
```

Expected:

```text
available
```

---

## Step 2 – Start Application Servers

```bash
aws autoscaling update-auto-scaling-group \
--auto-scaling-group-name NovaSyndicate-App-ASG \
--desired-capacity 2
```

Verify:

```bash
aws autoscaling describe-auto-scaling-groups \
--auto-scaling-group-names NovaSyndicate-App-ASG
```

Expected:

```text
Desired Capacity = 2
```

---

# 4. Stop Environment Procedure

## Step 1 – Stop Application Servers

```bash
aws autoscaling update-auto-scaling-group \
--auto-scaling-group-name NovaSyndicate-App-ASG \
--desired-capacity 0
```

---

## Step 2 – Stop Database

```bash
aws rds stop-db-instance \
--db-instance-identifier nova-syndicate-postgresql \
--region eu-west-3
```

---

# 5. Daily Operational Checks

## CloudWatch

Verify:

* No active alarms
* Healthy metrics

Command:

```bash
aws cloudwatch describe-alarms \
--state-value ALARM
```

---

## AWS Backup

Verify:

* Latest backup completed successfully

Command:

```bash
aws backup list-backup-jobs \
--by-backup-vault-name NovaSyndicate-Backup-Vault \
--region eu-west-3
```

---

## GuardDuty

Verify:

* No critical findings

Command:

```bash
aws guardduty list-detectors
```

---

## Security Hub

Verify:

* No unresolved critical findings

Command:

```bash
aws securityhub get-findings
```

---

## RDS

Verify:

* Status = available

---

## Auto Scaling Group

Verify:

* Healthy instances
* Desired capacity respected

---

# 6. Emergency Procedures

## EC2 Instance Failure

Recovery:

* ALB detects unhealthy target
* ASG replaces failed instance automatically

Expected Recovery Time:

2–5 minutes

---

## Database Failure

Recovery:

* Investigate CloudWatch alarms
* Restore database from AWS Backup if required

Expected Recovery Time:

2–4 hours

---

## Backup Failure

Recovery Steps:

1. Verify RDS status
2. Verify IAM Backup Role
3. Launch manual backup
4. Review Backup logs

---

## IAM Compromise

Recovery Steps:

1. Disable compromised credentials
2. Rotate access keys
3. Review CloudTrail logs
4. Review GuardDuty findings
5. Apply remediation actions

---

# 7. Automation

Health Check Script:

```bash
python3 automation/16-automation-health-check.py
```

Expected:

```text
GLOBAL STATUS: HEALTHY
```

---

# 8. Maintenance Schedule

| Task                | Frequency      |
| ------------------- | -------------- |
| Backup Verification | Daily          |
| CloudWatch Review   | Daily          |
| Security Hub Review | Daily          |
| GuardDuty Review    | Daily          |
| DRP Test            | Every 6 Months |
| BCP Review          | Every 6 Months |

---

# Approval

Nova Syndicate IT Department

Version: 1.0

Status: Approved