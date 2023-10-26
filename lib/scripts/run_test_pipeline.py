"""Script to setup the test data in postgres and connect it to the test dashboard in superset"""
from lib.data.data_source import DataSource
from lib.postgres.postgres import Postgres

# Checking
checking_list = ["date", "amount", "nothing", "nothing2", "description"]
checking_df = DataSource("CHECKING.csv", checking_list, False).read_spend_file()
# Savings
savings_list = ["date", "amount", "nothing", "nothing2", "description"]
savings_df = DataSource("SAVINGS.csv", savings_list, False).read_spend_file()
# Credit
credit_df = DataSource("CREDIT.csv", None, True).read_spend_file()


Postgres().read_in_dataframe("raw_checking", checking_df, "replace")
Postgres().read_in_dataframe("raw_savings", savings_df, "replace")
Postgres().read_in_dataframe("raw_credit", credit_df, "replace")

# merges data into raw_historical_tables and transformed historical
# run_postgres_sql_statements


# run sql to create custom categories and everything else.
# run_postgres_sql_statements for categories
