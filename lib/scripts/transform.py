import os
import pandas as pd

column_order = [
    "Type",
    "Date",
    "Amount",
    "Description",
    "Individual",
    "Month",
    "Year",
    "Day",
    "Flow",
]


def transform_financial_data():
    """Transforms some data"""

    parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

    # Construct the full path to the credentials file
    checking_path = os.path.join(parent_dir, "imports", "CHECKING.csv")
    saving_path = os.path.join(parent_dir, "imports", "SAVINGS.csv")
    credit_path = os.path.join(parent_dir, "imports", "CREDIT.csv")

    # Read the CSV file into a Pandas DataFrame
    checking_df = pd.read_csv(
        checking_path, names=["Date", "Amount", "nothing", "nothing2", "Description"]
    )
    saving_df = pd.read_csv(
        saving_path, names=["Date", "Amount", "nothing", "nothing2", "Description"]
    )
    credit_df = pd.read_csv(credit_path, header=[0])

    checking_df["Type"] = "CHECKING"
    saving_df["Type"] = "SAVINGS"
    credit_df["Type"] = "CREDIT"

    # credit transform
    credit_df = credit_df.rename(columns={"Member Name": "Individual"})

    credit_df["Debit"] = credit_df["Debit"] * -1
    credit_df["Credit"] = credit_df["Credit"] * -1
    credit_df["Amount"] = credit_df["Credit"].fillna(0) + credit_df["Debit"].fillna(0)

    # Other transforms

    checking_df["Individual"] = ""
    saving_df["Individual"] = ""

    checking_df["Flow"] = checking_df["Amount"].apply(lambda x: "In" if x > 0 else "Out")
    saving_df["Flow"] = saving_df["Amount"].apply(lambda x: "In" if x > 0 else "Out")
    credit_df["Flow"] = credit_df["Amount"].apply(lambda x: "In" if x > 0 else "Out")

    checking_df["NewDate"] = pd.to_datetime(checking_df["Date"])
    saving_df["NewDate"] = pd.to_datetime(saving_df["Date"])
    credit_df["NewDate"] = pd.to_datetime(credit_df["Date"])

    checking_df["Year"] = checking_df["NewDate"].dt.year
    checking_df["Month"] = checking_df["NewDate"].dt.month
    checking_df["Day"] = checking_df["NewDate"].dt.strftime("%A")

    saving_df["Year"] = saving_df["NewDate"].dt.year
    saving_df["Month"] = saving_df["NewDate"].dt.month
    saving_df["Day"] = saving_df["NewDate"].dt.strftime("%A")

    credit_df["Year"] = credit_df["NewDate"].dt.year
    credit_df["Month"] = credit_df["NewDate"].dt.month
    credit_df["Day"] = credit_df["NewDate"].dt.strftime("%A")

    checking_df = checking_df[column_order]
    saving_df = saving_df[column_order]
    credit_df = credit_df[column_order]

    total_df = pd.concat([checking_df, saving_df, credit_df])

    return total_df
