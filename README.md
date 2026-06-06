# Nova Syndicate – AWS Cloud Security & Infrastructure Modernization

## Project Overview

Nova Syndicate is a fictional logistics company specializing in the distribution of critical components for the medical, aerospace, and defense industries.

This project simulates a real-world cloud modernization engagement where a legacy infrastructure is redesigned using AWS best practices for security, scalability, resilience, automation, and operational excellence.

The objective is to transform a fragmented on-premise environment into a secure, highly available, and operationally mature AWS platform.

---

## Business Context

Nova Syndicate operates from:

* Headquarters: Lyon, France
* Regional Office: Marseille, France
* 20 Remote Employees

### Challenges

* No centralized identity management
* No monitoring platform
* No backup strategy
* No disaster recovery procedures
* Limited operational visibility
* Manual administration processes

### Objectives

* Centralize identity and access management
* Improve security posture
* Increase scalability and availability
* Implement monitoring and logging
* Establish business continuity and disaster recovery procedures
* Automate operational tasks

---

# Final Architecture

![Final Architecture](Architecture/SPRINT_4_NOVA.png)

---

# Sprint Overview

---

# Sprint 1 – Secure Cloud Foundation

![Sprint 1 Architecture](Architecture/SPRINT_1_NOVA.png)

## Objectives

Build a secure and scalable AWS foundation.

## Deliverables

* Multi-AZ VPC Architecture
* Public and Private Subnets
* Route Tables
* Security Groups
* IAM Foundations
* AWS KMS Encryption
* CloudTrail Logging
* AWS GuardDuty
* AWS Security Hub
* VPC Endpoints

## AWS Services

* VPC
* IAM
* KMS
* CloudTrail
* GuardDuty
* Security Hub
* VPC Endpoints

---

# Sprint 2 – Compute & Database Platform

![Sprint 2 Architecture](Architecture/SPRINT_2_NOVA.png)

## Objectives

Deploy a highly available application and database layer.

## Deliverables

* Launch Template
* Auto Scaling Group
* Application Load Balancer
* EC2 Private Instances
* PostgreSQL RDS
* CloudWatch Alarms
* Systems Manager Administration

## AWS Services

* EC2
* Auto Scaling
* Application Load Balancer
* RDS PostgreSQL
* Systems Manager
* CloudWatch

---

# Sprint 3 – Operations, Monitoring & Resilience

![Sprint 3 Architecture](Architecture/SPRINT_3_NOVA.png)

## Objectives

Improve observability, backup management, and operational resilience.

## Deliverables

* AWS Backup
* Backup Vault
* Backup Selection
* CloudWatch Dashboard
* Centralized Logging
* Enhanced Monitoring
* SNS Notifications

## AWS Services

* AWS Backup
* CloudWatch Dashboard
* CloudWatch Logs
* SNS
* CloudTrail

---

# Sprint 4 – Business Continuity, Disaster Recovery & Automation

![Sprint 4 Architecture](Architecture/SPRINT_4_NOVA.png)

## Objectives

Strengthen operational resilience through business continuity planning, disaster recovery procedures, automation, and operational documentation.

## Deliverables

### Business Continuity Plan (BCP)

* EC2 Failure Recovery
* Availability Zone Failure Recovery
* IAM Compromise Procedures
* Database Service Degradation Procedures

### Disaster Recovery Plan (DRP)

* RTO / RPO Definition
* Database Restore Procedures
* Backup Recovery Procedures
* Regional Disaster Strategy

### Automation

Python health-check script using boto3:

```bash
NOVA SYNDICATE HEALTH CHECK

RDS: OK
ASG: OK
ALB: OK
CloudWatch: OK
Backup: OK

GLOBAL STATUS: HEALTHY
```

### Operational Documentation

* Operational Runbook
* Startup Procedures
* Shutdown Procedures
* Daily Operational Checks
* Incident Response Procedures

## AWS Services

* AWS Backup
* CloudWatch
* CloudTrail
* GuardDuty
* Security Hub
* Systems Manager
* IAM
* RDS PostgreSQL

---

# Technology Stack

## Cloud Platform

* Amazon Web Services (AWS)

## Infrastructure as Code

* AWS CloudFormation

## Security

* IAM
* KMS
* CloudTrail
* GuardDuty
* Security Hub

## Monitoring & Logging

* CloudWatch
* CloudWatch Logs
* SNS

## Backup & Recovery

* AWS Backup
* Backup Vault
* RDS Snapshots

## Automation

* Python
* boto3

---

# Recovery Objectives

| Service             | RTO     | RPO      |
| ------------------- | ------- | -------- |
| Web Application     | 2 Hours | 24 Hours |
| PostgreSQL Database | 4 Hours | 24 Hours |
| Monitoring Platform | 4 Hours | 24 Hours |

---

# Security Features

* Principle of Least Privilege
* Encryption at Rest using AWS KMS
* Centralized Logging
* Audit Trails
* Threat Detection
* Security Monitoring
* Backup Protection
* Operational Runbooks

---

# Operational Resilience

## Business Continuity

* Auto Scaling Recovery
* Multi-AZ Architecture
* Incident Response Procedures
* Operational Documentation

## Disaster Recovery

* AWS Backup
* Recovery Procedures
* Backup Validation
* Future Cross-Region Strategy

---

# Repository Structure

```text
Architecture/
├── SPRINT_1_NOVA.png
├── SPRINT_2_NOVA.png
├── SPRINT_3_NOVA.png
└── SPRINT_4_NOVA.png

automation/
└── 16-automation-health-check.py

documentation/
├── Nova_Syndicate_BCP.md
├── Nova_Syndicate_DRP.md
└── Nova_Syndicate_Runbook.md

templates/
├── 01-network-foundation.yaml
├── 02-security-iam-kms.yaml
├── ...
└── backup-stack.yaml

README.md
```

---

# Skills Demonstrated

### Cloud Architecture

* AWS Architecture Design
* High Availability
* Scalability
* Infrastructure as Code

### Cloud Security

* IAM Design
* Encryption Management
* Threat Detection
* Security Monitoring

### Operations

* Monitoring & Alerting
* Backup Management
* Incident Response
* Operational Documentation

### Automation

* Python Scripting
* boto3 SDK
* Health Checks
* Infrastructure Validation

---

# Future Improvements

## Sprint 5 – DevSecOps & CI/CD

Planned enhancements:

* AWS CodePipeline
* AWS CodeBuild
* GitHub Integration
* Security Scanning
* Infrastructure Validation
* Automated CloudFormation Deployments
* DevSecOps Pipeline

---

# Author

**Lionel Mpata**

AWS Certified Solutions Architect – Associate

Cloud Security & AWS Architecture Enthusiast
