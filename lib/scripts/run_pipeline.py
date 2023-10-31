"""Main Pipeline Script"""
import logging
from datetime import date

from lib.data.data_source import DataSource
from lib.s3.s3 import S3Object

BUCKET = "personal-finance-imports"


def main():
    """Run processes"""
    checking_list = ["Date", "Amount", "nothing", "nothing2", "Description"]
    checking_source = DataSource("CHECKING.csv", checking_list, False)

    savings_list = ["Date", "Amount", "nothing", "nothing2", "Description"]
    savings_source = DataSource("SAVINGS.csv", savings_list, False)

    credit_source = DataSource("CREDIT.csv", None, True)

    S3Object().send_data_to_s3(
        checking_source.path,
        BUCKET,
        "checking/" + str(date.today()) + "-" + checking_source.file_name,
    )

    S3Object().send_data_to_s3(
        savings_source.path,
        BUCKET,
        "savings/" + str(date.today()) + "-" + savings_source.file_name,
    )

    S3Object().send_data_to_s3(
        credit_source.path,
        BUCKET,
        "credit/" + str(date.today()) + "-" + credit_source.file_name,
    )


if __name__ == "__main__":
    main()


# # Takes imports, transforms imports, takes google sheets existing data, dedups
# checking_dataset = DataSource('CHECKING.csv', ["Date", "Amount", "nothing", "nothing2", "Description"], False).read_spend_file()
