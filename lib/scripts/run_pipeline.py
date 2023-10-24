"""Main Pipeline Script"""
import logging
import os
import sys
from datetime import date


from lib.s3.s3 import S3Object
from lib.data.data_source import DataSource
from lib.postgres.postgres import Postgres


def main():
    """Run processes"""
    checking_list = ["Date", "Amount", "nothing", "nothing2", "Description"]
    checking_source = DataSource('CHECKING.csv', checking_list, False)
    
    try:
        S3Object().send_data_to_s3(checking_source.path, 'personal-finance-imports', str(date.today()) + "-" + checking_source.file_name)
        
    except Exception as err:
        logging.error("Something went wrong. %s", err)

if __name__ == "__main__":
    main()




# # Takes imports, transforms imports, takes google sheets existing data, dedups
# checking_dataset = DataSource('CHECKING.csv', ["Date", "Amount", "nothing", "nothing2", "Description"], False).read_spend_file()
