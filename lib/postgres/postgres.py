"""Postgres Class"""

import logging
import os

import psycopg2
from sqlalchemy import create_engine


class Postgres:
    """Class for Postgres data connection"""

    def __init__(self):
        self.conn = None

        self.username = os.environ["POSTGRES_USER"]
        self.password = os.environ["POSTGRES_PASSWORD"]
        self.db_name = os.environ["POSTGRES_DB"]
        self.schema = os.environ["POSTGRES_SCHEMA"]
        self.host = os.environ["POSTGRES_HOST"]
        self.port = os.environ["POSTGRES_PORT"]
        self.db_url = f"postgresql://{self.username}:{self.password}@{self.host}:{self.port}/{self.db_name}"

        self.db_params = {
            "host": self.host,
            "user": self.username,
            "password": self.password,
            "dbname": self.db_name,
            "port": self.port,
            "schema": self.schema,
        }

    def connect(self):
        """Establish a connection with psycopg2"""
        self.conn = psycopg2.connect(**self.db_params)
        return self.conn

    def read_in_dataframe(self, table_name, dataframe, strategy):
        """Take dataframe and put it into postgres"""

        engine = create_engine(self.db_url)
        dataframe.to_sql(
            table_name, engine, schema=self.schema, if_exists=strategy, index=False
        )

    def query(self, query):
        """Used to run a query"""
        cur = self.conn.cursor()
        try:
            cur.execute(query)
            self.conn.commit()  # Commit after each script execution
            logging.info("The query has been run successfully.")

        except psycopg2.DatabaseError as err:
            self.conn.rollback()
            logging.error("An error has occurred. %s", err)

        cur.close()
        self.conn.close()

    def run_scripts(self, scripts: list, sql_parent_path: str) -> None:
        """Used to run sql scripts"""

        cur = self.connect().cursor()
        for script in scripts:
            with open(sql_parent_path + script, "r", encoding="utf-8") as sql_file:
                sql_commands = sql_file.read()

            try:
                cur.execute(sql_commands)
                self.conn.commit()  # Commit after each script execution
                logging.info("The sql file %s has been run successfully.", script)

            except psycopg2.DatabaseError as err:
                self.conn.rollback()
                logging.error("An error has occurred. %s", err)

        # Close the cursor and connection
        cur.close()
        self.conn.close()
