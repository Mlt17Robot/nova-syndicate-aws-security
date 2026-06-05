# Nova Syndicate Disaster Recovery Plan (DRP)

## Version Information

| Field        | Value                  |
| ------------ | ---------------------- |
| Document     | Disaster Recovery Plan |
| Version      | 1.0                    |
| Status       | Approved               |
| Environment  | Production             |
| Last Updated | June 2026              |

---

# 1. Purpose

The purpose of this Disaster Recovery Plan (DRP) is to define the procedures required to restore Nova Syndicate's critical IT services following a major disruption, infrastructure failure, security incident, or data loss event.

This plan ensures that business operations can be restored within acceptable recovery objectives while minimizing operational and financial impact.

---

# 2. Scope

This Disaster Recovery Plan applies to all critical AWS services used by Nova Syndicate, including:

* Amazon EC2
* Auto Scaling Groups
* Application Load Balancer
* Amazon RDS PostgreSQL
* AWS Backup
* AWS CloudWatch
* AWS Systems Manager
* AWS Identity and Access Management (IAM)
* AWS CloudTrail
* AWS GuardDuty
* AWS Security Hub

---

# 3. Recovery Objectives

## Recovery Time Objective (RTO)

Maximum acceptable downtime before service restoration.

## Recovery Point Objective (RPO)

Maximum acceptable amount of data loss.

| Service             | RTO      | RPO      |
| ------------------- | -------- | -------- |
| Web Application     | 2 Hours  | 24 Hours |
| PostgreSQL Database | 4 Hours  | 24 Hours |
| Backup Services     | 24 Hours | 24 Hours |
| Monitoring Platform | 4 Hours  | 24 Hours |
| IAM Services        | 2 Hours  | N/A      |

---

# 4. Disaster Recovery Team

| Role                   | Responsibility          |
| ---------------------- | ----------------------- |
| Cloud Administrator    | Infrastructure recovery |
| Security Administrator | Incident investigation  |
| Operations Manager     | Business communication  |
| Executive Management   | Strategic decisions     |

---

# 5. Recovery Scenarios

---

## Scenario 1 – EC2 Instance Failure

### Description

An EC2 instance becomes unavailable due to software, hardware, or operating system failure.

### Impact

* Reduced application capacity

### Recovery Procedure

1. Application Load Balancer detects unhealthy instance.
2. Auto Scaling Group terminates failed instance.
3. Auto Scaling Group launches replacement instance.
4. New instance automatically joins the target group.
5. Verify application availability.

### Expected Recovery Time

2–5 minutes

### Recovery Method

Automatic

---

## Scenario 2 – PostgreSQL Database Corruption

### Description

Database corruption affects data integrity and application functionality.

### Impact

* Application unavailable
* Potential data loss

### Recovery Procedure

1. Identify corruption through monitoring alerts.
2. Stop application access.
3. Open AWS Backup Console.
4. Select latest valid recovery point.
5. Restore database instance.
6. Validate data integrity.
7. Redirect application traffic.

### Expected Recovery Time

2–4 hours

### Recovery Method

AWS Backup Restore

---

## Scenario 3 – Accidental Deletion of Database

### Description

Database deleted accidentally by administrator error.

### Impact

* Complete service interruption

### Recovery Procedure

1. Access AWS Backup Vault.
2. Locate latest recovery point.
3. Restore RDS instance.
4. Reconfigure application connection.
5. Validate application functionality.

### Expected Recovery Time

2–4 hours

### Recovery Method

Backup Recovery

---

## Scenario 4 – Availability Zone Failure

### Description

An AWS Availability Zone becomes unavailable.

### Impact

* Partial service degradation

### Recovery Procedure

1. ALB routes traffic to healthy Availability Zone.
2. Auto Scaling Group launches replacement instances.
3. Verify application performance.
4. Monitor AWS Health Dashboard.

### Expected Recovery Time

5–10 minutes

### Recovery Method

Automatic High Availability Recovery

---

## Scenario 5 – IAM Credential Compromise

### Description

Unauthorized access is detected using compromised IAM credentials.

### Impact

* Security breach
* Potential data exposure

### Recovery Procedure

1. Disable compromised account immediately.
2. Revoke active sessions.
3. Rotate credentials.
4. Review CloudTrail activity.
5. Investigate GuardDuty findings.
6. Review Security Hub recommendations.
7. Apply remediation actions.
8. Restore access only after validation.

### Expected Recovery Time

Less than 2 hours

### Recovery Method

Security Incident Response

---

## Scenario 6 – AWS Systems Manager Unavailable

### Description

Loss of remote administration capabilities.

### Impact

* Reduced operational management

### Recovery Procedure

1. Verify AWS Service Health Dashboard.
2. Escalate to AWS Support if necessary.
3. Use emergency administrative procedures.
4. Monitor service restoration.

### Expected Recovery Time

Dependent on AWS service availability.

---

## Scenario 7 – Regional Disaster

### Description

Complete loss of AWS Region eu-west-3.

### Impact

* Total infrastructure outage

### Recovery Procedure

1. Activate disaster declaration process.
2. Restore backups in secondary AWS Region.
3. Deploy infrastructure using CloudFormation templates.
4. Restore database backups.
5. Validate application functionality.
6. Redirect DNS traffic.

### Expected Recovery Time

24–48 hours

### Recovery Method

Cross-Region Disaster Recovery Strategy

### Future Improvement

Implement cross-region backup replication between:

* Primary Region: eu-west-3 (Paris)
* Secondary Region: eu-west-1 (Ireland)

---

# 6. Backup Strategy

## Backup Platform

AWS Backup

## Protected Resources

* Amazon RDS PostgreSQL
* EC2 instances tagged:

  * Backup = true

## Backup Frequency

Daily

## Retention Period

35 Days

## Encryption

AWS KMS

## Backup Verification

Daily verification of successful backup jobs.

---

# 7. Monitoring and Detection

The following services provide disaster detection capabilities:

* Amazon CloudWatch
* AWS CloudTrail
* AWS Backup
* AWS GuardDuty
* AWS Security Hub

Alerts must be investigated immediately by the Cloud Operations team.

---

# 8. Recovery Validation

After every recovery operation:

1. Verify application accessibility.
2. Verify database connectivity.
3. Validate business transactions.
4. Review CloudWatch metrics.
5. Confirm user access functionality.

Recovery is considered successful only after all validation checks have passed.

---

# 9. Testing Schedule

Disaster Recovery testing must be performed:

* Every 6 months
* After major infrastructure changes
* After any significant security incident

Testing results must be documented and reviewed.

---

# 10. Continuous Improvement

The Disaster Recovery Plan must be updated whenever:

* Infrastructure changes occur
* New AWS services are introduced
* Security incidents reveal weaknesses
* Recovery objectives change

---

# Approval

Nova Syndicate IT Department

Version: 1.0

Status: Approved
