# personal-finance-automation
![Finance Tree](https://github.com/sam-wright-1/personal-finance-automation/blob/main/images/finance.jpg)                                                       

# Requirements
* Docker Installation
* Intermediate Python and SQL skills
  
# Quickstart
1. Clone this repo:
   1. `git clone https://github.com/sam-wright-1/personal-finance-automation.git`
   2. In the repo, run `docker compose up -d`
   3. Once initialized and containers are running, you can run `docker exec -it finance_python python3 lib/scripts/run_test_pipeline.py` which builds some test data into postgres tables.
3. Download Apache Superset using Docker Compose (https://superset.apache.org/docs/installation/installing-superset-using-docker-compose/)
   1. Run `git clone https://github.com/apache/superset.git`
   2. Run `cd superset`
   3. For Mac run
      ```
      docker compose -f docker-compose-non-dev.yml pull
      docker compose -f docker-compose-non-dev.yml up
      ```
      For Windows run
      ```
      git checkout 3.0.0
      set TAG=3.0.0
      docker compose -f docker-compose-non-dev.yml pull
      docker compose -f docker-compose-non-dev.yml up
      ```
4. Log into apache superset by going to localhost:8088 in your browser and using `admin` as both the username and password 
5. Import the test dashboard using the zip file located at `lib/superset/resources/personal_finance_test_dashboard.zip`.
   1. open superset and go to the "Dashboard" tab. Click on the "Import" button and select the zip file.
   2. Click on the Import button and use `postgres` as the password if it asks for one (default password that allows you to connect to postgres as that is the database connection source)
   3. Go to the dashboard and make sure that data is appearing in the graphs.  You may have to refresh your page or the dashboard.

___


# Purpose
* Guide users to create a free, semi-automated financial system with code.
* Create your own data engineering project using many tools and methods that are highly utilized in practice (Docker, Docker Compose, Superset, Airbyte, object-oriented programming, etc)
* This project streamlines your financial spending data, subjecting it to a series of transformations before presenting it in an accessible dashboard capable of providing answers to a wide array of financial questions.  All of this is containerized so its easy to use and rebuild if needed.

### What the dashboard might look like 
![Finance Arch](https://github.com/sam-wright-1/personal-finance-automation/blob/main/images/financial_snapshot.jpg)

# Benefit
#### At the end of this guide you will have created:
* A dashboard that will help you answer basic questions such as "How much money do I spend on x category on average per month?" or "How much money did I make this year compared to how much money did I spend?"
* An easy way to update your spend financial data (takes ~ 1 or 2 minutes).
* Your own basic data engineering project.

# Detailed Explainations
* `lib/imports` holds data that you export from your financial sources.  This data will be transformed and put into whatever storage you choose.
* `lib/superset` used to interface with superset 
* `lib/s3.py` used to interface with s3
* `lib/postgres/sql` holds all of the sql code to transform raw data in postgres to a usable format.
* `lib/airbyte` holds object code to interface with Airbyte
* `lib/scripts/run_test_pipeline.py` is used to run the transformation pipeline for test data that has been provided and put it into postgres for superset to read.  
* `lib/data` Holds the DataSource object that can be used for each source file that you need to upload
* `lib/google_sheets` holds credentials and code to interface with google sheets
* `lib/postgres` holds dockerfile for postgres code for postgres container and postgres data access object
* `lib/docker/Dockerfile` used to create the python container to run any scripts

# Solution Architecture
![Finance Arch](https://github.com/sam-wright-1/personal-finance-automation/blob/main/images/finance_architecture_diagram.png)

# Components
### Using Airbyte
Using airbyte, you can create pipelines that push data to google sheets or s3, and then you can have airbyte push that data to postgres for superset to read from.
1. Clone Airbyte into this repo (from https://docs.airbyte.com/quickstart/deploy-airbyte/)
   1. `git clone https://github.com/airbytehq/airbyte.git`
   2. `cd airbyte`
   3. `./run-ab-platform.sh`
   4. Go to localhost:8000 in your browser and use username:airbyte, password:password
   5. Youll need to create connections to the systems of your choice manually.
2. **_IMPORTANT_** - In order for you python container to access the airbyte container, you have to connect them through an external network.  To do this you will need to do the following:
   1. If the external network doesnt exist, create with `docker network create --driver bridge my_custom_network`
   2. Add this network to the docker container called `airbyte-proxy` in the networks section.  This should allow the python container to access the airbyte container through requests
3. Using Airbyte with google sheets
   1. Go to localhost:8000 and login to airbyte (airbyte, password)
      - Create a source with google sheets
      - Input client id, secret, and refresh token that you received from your google cloud project steps (see Using Google Sheets section below)
      - If that doesnt work, you can try created a service account in Google Cloud
      - Create a destination with Postgres using correct postgres creds.
      - Create a connection between google sheets and postgres with the sheets you want to sync.
      - Make a note of the connectionid of the connection just created (can be found in the url) and use that in `lib/airbyte/airbyte.py` for connectionId in the payload (which is currently empty)
  
### Using Google Sheets
Google sheets can be used as a raw or transformed data storage that airbyte can push to postgres for an easy data pipeline integration
1. Create Google Sheet for Personal Finance
   - This is just to house all of your data.  You can look at my google sheet image to get an idea of what columns I included in mine.  `images/sheet_image.png`
2. Create Google Cloud Project
   1. Enable Google Sheets API under APIs and Services
   2. In the same spot (APIs and Services), under credentials, create OAuth 2.0 client credentials
      - Basically just follow this https://developers.google.com/sheets/api/quickstart/python
      - You'll have to donwload and rename the .json credentials file as credentials.json
      - Put credentials in lib/google_sheets/creds as `credentials.json`
      - Once you run the google sheets code, it will have you authenticate through your browser so that your python code can access google sheets.
      - Once authenticated it should create a `token.json` file in the creds directory that will be used going forward.
      - If you ever get an error that says that the credentials are invalid or need to be refreshed, you can delete the `token.json` file and reauthenticate
### Using S3
S3 can be used to store all of your data in the cloud (first few gigabytes of data are free which personal spend shouldnt ever reach that much data)
1. Make sure that the following vars are set in your environment:
```
AWS_ACCESS_KEY_ID=
AWS_SECRET_ACCESS_KEY=
AWS_DEFAULT_REGION=
```
2. boto3 will use the vars to connect to s3
3. More to come
   
### Transformations
1. Modifications
   1. Any data you want to import should go into lib/imports as csv files
   2. You'll have to create your own transformations for your data based on how it comes in raw and how you want to categorize things.
   3. I recommend starting with just postgres and superset.  You can use the DataSource object in `lib/data/DataSource.py` to import your sources into postgres, and then using sql, transform the raw data to a usable format.
   4. If you want different categories, look for `lib/postgres/sql/create_categories.sql`.  This holds the custom code to map out your categories based on the descriptions from your data sources.
   5. The file `lib/scripts/transform.py` shows some python transformations that can be used.  Maybe adding a new method to the object DataSource in `lib/data/datas_source.py` would work easier than using this script

### Tips for Superset
1. If you right click on any of the bars on any bar chart, you can choose to drill down to the line items within that bar, making it very easy to answer quick questions.
2. The top right hand corner should have an ellipsis which allows you to refresh the dashboard 
3. Filters can be incredibly helpful, which is why they are in the test dashboard.  The show up on the left hand side and let you choose to filter by dates, categories, types, etc.
  
### Environment Variables
If you want to overwrite any env variables, create a .env file with any of the following vars included
   ```
   # Airbyte env
   AIRBYTE_HOST=
   AIRBYTE_USER=
   AIRBYTE_PASSWORD=
   AIRBYTE_PORT=8000
   
   # Superset env
   SUPERSET_HOST=
   SUPERSET_USERNAME=
   SUPERSET_PASSWORD=
   SUPERSET_PORT=8088
   
   # Postgres env
   POSTGRES_DB=
   POSTGRES_HOST=
   POSTGRES_USER=
   POSTGRES_PASSWORD=
   POSTGRES_PORT=
   POSTGRES_SCHEMA=
   
   AWS_ACCESS_KEY_ID=
   AWS_SECRET_ACCESS_KEY=
   AWS_DEFAULT_REGION=
   
   PYTHONPATH=
   ```

# Future
* Linting, formatting, unit and integration tests
* More interchangable parts to accommodate many cases
* Better way to categorize spend besides like statements (probably some lookup / config tables in postgres that can be modified)

