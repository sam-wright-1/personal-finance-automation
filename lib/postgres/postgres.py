"""Postgres Class"""

import os
import logging
import psycopg2

class Postgres:
  """Class for Postgres data connection"""

  def __init__(self):
      self.conn = None
      
      self.username = os.environ['USERNAME']
      self.password = os.environ['PASSWORD']
      self.db_name = os.environ['DB_NAME']
      self.host = os.environ['HOST']
      
      self.db_params = {
      "host": self.host,
      "user": self.username,
      "password": self.password,
      "dbname": self.db_name
  }

  def connect(self):
    """Establish a connection with psycopg2"""
    self.conn = psycopg2.connect(self.db_params)
    return self.conn

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

