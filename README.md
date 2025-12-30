Home3-Scheduler

Care facilities currently manage appointments across multiple homes, clients, and caregivers manually.
Manual reminder systems frequently fail, leading to missed appointments, operational disruption,
and increased costs. This project addresses that reliability gap through automated, observable scheduling. 

Architecture-Stack
AWS Service Used:
Lambda - Executes reminder processing logic with structured logging.
Eventbridge - Triggers reminders on scheduled periods.
DynamoDB - Stores appointment data
SNS - Delivers notifications to staff & clients
CloudWatch - Centralized logging and metrics for appointments

Design Principles: Observability over features, Failure-first design

Core Workflow:
1. EventBridge rule triggers at scheduler reminder time
2. Lambda function retrieves an appointment from DynamoDB
3. Lambda publishes a notification to the SNS topic
4. SNS delivers a reminder to staff/ clients
5. All events logged to CloudWatch

Failure Scenarios: 
- Eventbridge misconfig - Incorrect cron expression prevents trigger
- IAM permissions gaps - Lambda is unable to publish to SNS.
- Silent failures - Missing observability prevents detection.

Workflow of appointment feature
1. Create appointment --> status: scheduled
2. Edit appointment --> old deleted, new added
3. Cancelled appointment --> status: cancelled
4. Failed appointment --> status: failed, error logged and evaluated for cause.
5. 
