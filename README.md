# HalifaxTaxi-Order-Processing-with-SQS-SNS
Order Processing with AWS Lambda, SQS, and SNS: Develop an efficient order processing system for HalifaxTaxi, an online car delivery service, using AWS Lambda, SQS, and SNS. Streamline order management, notification triggers, and client communication for a seamless user experience.

---

## Overview

Welcome to the HalifaxTaxi Order Processing repository. This professional project showcases the development of an order processing system using AWS services, specifically Lambda, SQS, and SNS. The application is designed to enhance the user experience for an online car delivery service, ensuring timely order processing, efficient management, and seamless communication.

### Features

- **Order Queue:** Orders from customers are added to a standard SQS queue.
- **Random Order Generation:** A simulated program sends random order messages, including car type, accessories, and street address, to HalifaxTaxi's queue.
- **Order Monitoring:** Bob, the owner, periodically checks for orders in the queue using a Lambda function.
- **Notification Service:** Upon order availability, an SNS notification is triggered, sending order details to your email for car delivery.

### Workflow

1. Simulated program generates random order messages and sends them to HalifaxTaxi's order queue.
2. Bob periodically checks the order queue for new orders.
3. Upon detecting an order, an SNS notification is triggered, sending order details to your email.
4. You, as the car delivery service provider, receive the notification and deliver the car to the client's address.

![image](https://github.com/AlagappanVeerappan32/HalifaxTaxi-Order-Processing-with-SQS-SNS/assets/133504573/d28918cf-3d20-460c-a7a5-3468182becc8)


### Testing

The application has undergone rigorous testing to ensure the seamless flow of order processing, monitoring, and notifications. Test cases have been designed to verify each stage of the process, from order generation to email notifications.

---

## How to Use

1. Clone this repository
2. Explore and modify Lambda function code to match your requirements.
3. Configure AWS services (SQS, SNS, Lambda) based on the provided steps.
4. Simulate order generation and monitoring to verify proper functionality.
