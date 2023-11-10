"""Script to setup the test data in postgres and connect it to the test dashboard in superset"""
from lib.data.data_source import DataSource
from lib.postgres.postgres import Postgres

def main():
    postgres_connection = Postgres()
    
    sql_statements = [
        "restart.sql"
    ]
    
    postgres_connection.run_scripts(sql_statements, "lib/postgres/sql/")

if __name__ == "__main__":
    main()
