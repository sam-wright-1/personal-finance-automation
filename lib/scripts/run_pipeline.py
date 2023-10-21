"""Main Pipeline Script"""
import logging
import os
import sys

from lib.scripts.transform import transform_financial_data
from lib.postgres.postgres import Postgres



def main():
    """Run processes"""
    try:
        # Takes imports, transforms imports, takes google sheets existing data, dedups
        new_data = transform_financial_data()

        print(Postgres().connect().query("select 'test';"))
        
    except Exception as err:
        logging.info("Something went wrong. %s", err)

    print('got here')
if __name__ == "__main__":
    main()
