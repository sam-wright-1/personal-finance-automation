# personal-finance-automation
![Finance Tree](https://github.com/sam-wright-1/personal-finance-automation/blob/main/lib/images/finance.jpg)                                                       

# Purpose
* The purpose of this repo is to help users create a free, semi-automated financial system with code.
* It will help you answer basic questions such as "How much money do I spend on x category on average per month?" or "How much money did I make this year compared to how much money did I spend?"

# Reward
#### At the end of this guide you will have created:
* A dashboard that will show you personal monthly spend totals, averages, and anything else you need to answer your basic financial questions.
* An easy way to update your financial data within one or two minutes.
* Your own basic data engineering project.

![Finance Arch](https://github.com/sam-wright-1/personal-finance-automation/blob/main/lib/images/financial_snapshot.png)

# Requirements
* Docker Installation
* Google Cloud Project
* Coding Basics

# Solution Architecture
![Finance Arch](https://github.com/sam-wright-1/personal-finance-automation/blob/main/lib/images/Finance%20Architecture.png)

# Steps to create solution
1. Clone Airbyte repo into this repo (from https://docs.airbyte.com/quickstart/deploy-airbyte/)
   1. git clone https://github.com/airbytehq/airbyte.git
   2. cd airbyte
   3. ./run-ab-platform.sh
   4. Go to localhost:8000 and use username:airbyte, password:password
2. Clone Superset repo into this repo (from https://superset.apache.org/docs/installation/installing-superset-using-docker-compose/)
   1. git clone https://github.com/apache/superset.git
   2. cd superset
   3. docker compose up
   4. Go to localhost:8088 and use username:admin, password:admin
3. Create Google Cloud Project
   1. Create a service 


