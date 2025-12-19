Home3-Scheduler

Care facilities currently manage appointments across multiple homes, clients, and caregivers manually.
Manual reminder systems frequently fail, leading to missed appointments, operational disruption,
and increased costs. This project addresses that reliability gap through automated, observable scheduling. 

Architecture

Core Services:
- AWS Lambda - Executes reminder processing logic with structured logging.
- Amazon Eventbridge - Triggers reminders on schedule
- Amazon DynamoDB - Stores appointment data
- Amazon SNS - Delivers notifications to staff & clients
- Amazon CloudWatch - Centralized logging and metrics

Design Principles: Observability over features, Failure-first design, Support-oriented debugging

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
