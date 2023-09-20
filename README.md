# personal-finance-automation
![Finance Tree](https://github.com/sam-wright-1/personal-finance-automation/blob/main/lib/images/finance.jpg)                                                       

# Purpose
* The purpose of this repo is to help users create a free, semi-automated financial system with code.
* It will help you answer basic questions such as "How much money do I spend on x category on average per month?" or "How much money did I make this year compared to how much money did I spend?"

# Benefit
#### At the end of this guide you will have created:
* A dashboard that will show you personal monthly spend totals, averages, and anything else you need to answer your basic financial questions.
* An easy way to update your financial data within one or two minutes.
* Your own basic data engineering project.

![Finance Arch](https://github.com/sam-wright-1/personal-finance-automation/blob/main/lib/images/financial_snapshot.png)

# Explaination
* You will use Google Sheets as your base for your financial data (i.e. your raw data should live here)
* lib/scripts/google_sheets.py takes the data provided by you (exported from financial sources) and imports it into a google sheet (with deduplication handled)
* lib/scripts/transform.py is used by lib/scripts/google_sheets.py and transforms the data that you provide in the imports folder.  You will most likely have to change this.
* lib/sql hold all of the sql transformations used to take the raw data that is imported into postgres through Airbyte and turn it into something that Superset can use.  It also categorizes your spend by description.
* lib/scripts/airbyte basically is just run when you want to replicate data from google sheets to postgres
* lib/scripts/run_sql_in_python.py is used to run the scripts in lib/sql in the postgres container
* lib/main.py puts everything together (takes data from lib/import, compares it to google sheets, inserts data into google sheets, then runs airbyte to push that data to postgres, then runs the sql commands in postgres to transform the data).
* lib/creds holds credentials to access google sheets through python
* postgres holds dockerfile for postgres container
* Data in Postgres is then used in Superset to create financial dashboard.

# Requirements
* Python Installation
* Docker Installation
* Google Cloud Project
* Coding Basics

# Solution Architecture
![Finance Arch](https://github.com/sam-wright-1/personal-finance-automation/blob/main/lib/images/finance_architecture.png)

# Steps to create solution
1. Clone Airbyte repo into this repo (from https://docs.airbyte.com/quickstart/deploy-airbyte/)
   1. `git clone https://github.com/airbytehq/airbyte.git`
   2. `cd airbyte`
   3. `./run-ab-platform.sh`
   4. Go to localhost:8000 in your browser and use username:airbyte, password:password
2. Clone Superset repo into this repo (from https://superset.apache.org/docs/installation/installing-superset-using-docker-compose/)
   1. `git clone https://github.com/apache/superset.git`
   2. `cd superset`
   3. `docker compose up`
   4. Go to localhost:8088 in your browser and use username:admin, password:admin
3. Create Postgres Container
   - `cd postgres`
   - `docker build -t personal_finance_postgres ./` (creates the docker image based on the Dockerfile in that folder)
   - `docker run -d --name personal_finance_postgres -p 5432:5432 personal_finance_postgres` (creates the container with the image you created)
   - Those commands will start the container up, but if you need to stop it or run it, you can use docker desktop or use docker commands (like `docker run CONTAINER_NAM`E or `docker stop CONTAINER_NAME`)
4. Create Google Sheet for Personal Finance
   - This is just to house all of your data.  You can look at my google sheet image to get an idea of what columns I included in mine.  (lib/images/sheet_image.png)
5. Create Google Cloud Project
   1. Enable Google Sheets API under APIs and Services
   2. In the same spot (APIs and Services), under credentials, create OAuth 2.0 client credentials
      - Basically just follow this https://developers.google.com/sheets/api/quickstart/python
      - You'll have to donwload and rename the .json credentials file as credentials.json
      - Put credentials in lib/creds as credentials.json
6. Modifications
   1. Any data you want to import should go into lib/imports as csv files
   2. Modify lib/scripts/google_sheets.py to include the id of the google sheet you want to use (which can be found in the url of the sheet), as well as the range of the sheet.  Also change any transformations in that file or lib/scripts/transform.py to whatever you need
   3. Make sure that all of the correct packages are installed.  (run `pip install -r requirements.txt` when in parent directory)
   5. Youll have to run the python script first to get a refresh token back, so you can run the script lib/scripts/google_sheets.py to get that.  A file called token.json should appear once that is done.
7. Connect in Airbyte 
   1. Go to localhost:8000 and login to airbyte (airbyte, password)
      - Create a source with google sheets
      - Input client id, secret, and refresh token that you received
      - If that doesnt work, you can try created a service account in Google Cloud
      - Create a destination with Postgres using correct postgres creds.
      - Create a connection between google sheets and postgres with the sheets you want to sync.
      - Make a note of the connectionid of the connection just created (can be found in the url) and use that in lib/scripts/airbyte.py for connectionId in the payload
8. Connect in Superset
    1. Go to localhost:8088 and login (admin, admin)
    2. Create a new database connection (can do from settings on the top right)
    3. Connect with correct postgres creds
    4. Start creating datasets from tables in postgres (starting with your raw data)
9. Run `main.py`
 
# NOTES:
   - When doing these steps, the containers state should be running.
   - Depending on how your data looks, you might have to do quite a few manual changes.
   - lib/sql holds sql scripts to create tables in postgres, make sure those make sense to run in postgres once data in replicated to the postgres container through airbyte

