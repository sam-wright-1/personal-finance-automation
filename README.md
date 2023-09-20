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
* Python Installation
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
   1. Enable Google Sheets API under APIs and Services
   2. In the same spot (APIs and Services), under credentials, create OAuth 2.0 client credentials
      - Basically just follow this https://developers.google.com/sheets/api/quickstart/python
      - You'll have to donwload and rename the .json credentials file as credentials.json
      - Put credentials in lib/creds as credentials.json
4. Modifications
   1. Any data you want to import should go into lib/imports as csv files
   2. Modify lib/scripts/google_sheets.py to include the id of the google sheet you want to use, as well as the range of the sheet.  Also change any transformations in that file or lib/scripts/transform.py to whatever you need
   3. Make sure that all of the correct packages are installed.  (run pip install -r requirements.txt when in parent directory)
   5. Youll have to run the python script first to get a refresh token back, so you can run the script lib/scripts/google_sheets.py to get that.  A file called token.json should appear once that is done.
5. Connect in Airbyte 
   1. Go to localhost:8000 and login to airbyte (airbyte, password)
      - Create a connection with google sheets
      - Input client id, secret, and refresh token that you received
      - If that doesnt work, you can try created a service account in Google Cloud
      - Create a connection with Postgres using correct postgres creds.
6. Connect in Superset
   1. Go to localhost:8088 and login (admin, admin)
   2. Create a new database connection (can do from settings on the top right)
   3. Connect with correct postgres creds
7. 

