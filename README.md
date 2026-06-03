# Nova Syndicate – AWS Infrastructure Modernization

## Overview

Nova Syndicate is a logistics company specializing in the distribution of critical components for the medical, aerospace, and defense sectors.

This project simulates a real-world cloud modernization initiative focused on:

* Security
* Scalability
* Monitoring
* Automation
* Business Continuity
* Disaster Recovery

---

# Sprint 1 – Secure Cloud Foundation

### Architecture

![Sprint 1 Architecture](Architecture/SPRINT_1_NOVA.png)

## Objectives

Build a secure AWS foundation with network segmentation, monitoring, and security controls.

### Implemented Services

* Amazon VPC
* Public & Private Subnets
* Internet Gateway
* NAT Gateway
* Route Tables
* Security Groups
* NACLs
* AWS KMS
* AWS CloudTrail
* Amazon GuardDuty
* AWS Security Hub
* VPC Endpoints

---

# Sprint 2 – Compute & Database Platform

### Architecture

![Sprint 2 Architecture](Architecture/SPRINT_2_NOVA.png)

## Objectives

Deploy the application and database layers with secure administration.

### Implemented Services

* IAM Roles
* Instance Profiles
* Launch Templates
* Application Load Balancer
* Target Groups
* Auto Scaling Group
* Amazon EC2
* AWS Systems Manager
* Amazon RDS PostgreSQL
* CloudWatch Metrics

---

# Sprint 3 – Operations, Monitoring & Resilience

### Architecture

![Sprint 3 Architecture](Architecture/SPRINT_3_NOVA.png)

## Objectives

Improve observability, alerting, centralized logging and backup strategy.

### Implemented Services

#### Monitoring

* CloudWatch Dashboard
* CloudWatch Alarms
* SNS Notifications

#### Logging

* CloudWatch Logs
* Application Logs
* Security Logs
* SSM Logs
* Metric Filter (ERROR)

#### Resilience

* AWS Backup Vault
* Backup Plan
* Backup Selection
* Automated Backups

---

# Current Architecture Features

* Bastionless administration using Systems Manager
* No SSH exposure
* Private EC2 instances
* Encrypted PostgreSQL database
* Centralized logging
* Real-time monitoring
* Automated backups
* Security monitoring

---

# Next Phase

Sprint 4 – Business Continuity, Disaster Recovery & Automation

Planned deliverables:

* BCP
* DRP
* RTO/RPO definition
* Automation scripts
* Operational runbooks
