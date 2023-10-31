"""Script to setup the test data in postgres and connect it to the test dashboard in superset"""
from lib.data.data_source import DataSource
from lib.postgres.postgres import Postgres


def main():
    """Run run test pipeline"""
    # Checking
    checking_list = ["date", "amount", "nothing", "nothing2", "description"]
    checking_df = DataSource("CHECKING.csv", checking_list, False).read_spend_file()
    # Savings
    savings_list = ["date", "amount", "nothing", "nothing2", "description"]
    savings_df = DataSource("SAVINGS.csv", savings_list, False).read_spend_file()
    # Credit
    credit_df = DataSource("CREDIT.csv", None, True).read_spend_file()

    source_list = {
        "raw_checking": checking_df,
        "raw_savings": savings_df,
        "raw_credit": credit_df,
    }
    postgres_connection = Postgres()
    for name, source_dataframe in source_list.items():
        postgres_connection.read_in_dataframe(name, source_dataframe, "replace")

    sql_statements = [
        "merge_checking.sql",
        "merge_savings.sql",
        "merge_credit.sql",
        "create_transformed_historical.sql",
        "create_categories.sql",
        "create_sum_category.sql",
        "dupe_validation.sql",
    ]

    postgres_connection.run_scripts(sql_statements, "lib/postgres/sql/")


if __name__ == "__main__":
    main()
