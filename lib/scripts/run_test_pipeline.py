"""Script to setup the test data in postgres and connect it to the test dashboard in superset"""
from lib.data.data_source import DataSource
from lib.postgres.postgres import Postgres

# Checking
checking_list = ["Date", "Amount", "nothing", "nothing2", "Description"]
checking_df = DataSource("CHECKING.csv", checking_list, False).read_spend_file
# Savings
savings_list = ["Date", "Amount", "nothing", "nothing2", "Description"]
savings_df = DataSource("SAVINGS.csv", savings_list, False).read_spend_file
# Credit
credit_df = DataSource("CREDIT.csv", None, True).read_spend_file


Postgres().read_in_dataframe("raw_checking", checking_df, "replace")
Postgres().read_in_dataframe("raw_savings", savings_df, "replace")
Postgres().read_in_dataframe("raw_credit", credit_df, "replace")

# strat (replace a raw source, run sql to transform to normalized thing, then merge to big table (maybe merge to both big raw table, and big normalized table to have both))
# 

# Create DataFrame
df = pd.DataFrame(data)
df.to_sql("data", con=conn, if_exists="replace", index=False)
conn = psycopg2.connect(conn_string)
conn.autocommit = True
cursor = conn.cursor()

sql1 = """select * from data;"""
cursor.execute(sql1)
for i in cursor.fetchall():
    print(i)

# conn.commit()
conn.close()
