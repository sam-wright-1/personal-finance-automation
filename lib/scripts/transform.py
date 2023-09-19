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
    citi_path = os.path.join(parent_dir, "imports", "CITIBANK.csv")

    # Read the CSV file into a Pandas DataFrame
    checking_df = pd.read_csv(
        checking_path, names=["Date", "Amount", "nothing", "nothing2", "Description"]
    )
    saving_df = pd.read_csv(
        saving_path, names=["Date", "Amount", "nothing", "nothing2", "Description"]
    )
    citi_df = pd.read_csv(citi_path, header=[0])

    checking_df["Type"] = "CHECKING"
    saving_df["Type"] = "SAVINGS"
    citi_df["Type"] = "CITIBANK"

    # Citi transform
    citi_df = citi_df.rename(columns={"Member Name": "Individual"})

    citi_df["Debit"] = citi_df["Debit"] * -1
    citi_df["Credit"] = citi_df["Credit"] * -1
    citi_df["Amount"] = citi_df["Credit"].fillna(0) + citi_df["Debit"].fillna(0)

    # Other transforms

    checking_df["Individual"] = ""
    saving_df["Individual"] = ""

    checking_df["Flow"] = checking_df["Amount"].apply(lambda x: "In" if x > 0 else "Out")
    saving_df["Flow"] = saving_df["Amount"].apply(lambda x: "In" if x > 0 else "Out")
    citi_df["Flow"] = citi_df["Amount"].apply(lambda x: "In" if x > 0 else "Out")

    checking_df["NewDate"] = pd.to_datetime(checking_df["Date"])
    saving_df["NewDate"] = pd.to_datetime(saving_df["Date"])
    citi_df["NewDate"] = pd.to_datetime(citi_df["Date"])

    checking_df["Year"] = checking_df["NewDate"].dt.year
    checking_df["Month"] = checking_df["NewDate"].dt.month
    checking_df["Day"] = checking_df["NewDate"].dt.strftime("%A")

    saving_df["Year"] = saving_df["NewDate"].dt.year
    saving_df["Month"] = saving_df["NewDate"].dt.month
    saving_df["Day"] = saving_df["NewDate"].dt.strftime("%A")

    citi_df["Year"] = citi_df["NewDate"].dt.year
    citi_df["Month"] = citi_df["NewDate"].dt.month
    citi_df["Day"] = citi_df["NewDate"].dt.strftime("%A")

    checking_df = checking_df[column_order]
    saving_df = saving_df[column_order]
    citi_df = citi_df[column_order]

    total_df = pd.concat([checking_df, saving_df, citi_df])

    return total_df
