"""File to manage data source class for all data sources"""

import logging
import os

import pandas as pd


class DataSource:
    """Class for any datasource that needs to be transformed and pushed into system"""

    def __init__(
        self, file_name: str, file_columns: list = None, includes_header: bool = False
    ):
        self.file_name = file_name
        self.spend_type = file_name.rstrip(".csv")
        self.path = self.set_path()
        self.column_names = file_columns
        self.has_header = includes_header

    def read_spend_file(self):
        """Pull in dataset to pandas"""
        logging.info("Reading in dataset")
        if self.has_header:
            return pd.read_csv(self.path, header=[0])

        return pd.read_csv(self.path, names=self.column_names)

    def set_path(self):
        """create parent_path"""
        parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        return os.path.join(parent_dir, "imports", self.file_name)
