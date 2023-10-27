"""Class for Superset"""

import logging
import os

import requests


class Superset:
    """Class for Superset"""

    def __init__(self):
        self.session = requests.Session()
        self.port = os.environ["SUPERSET_PORT"]
        self.host = os.environ["SUPERSET_HOST"]
        self.username = os.environ["SUPERSET_USERNAME"]
        self.password = os.environ["SUPERSET_PASSWORD"]
        self.url = f"http://{self.host}:{self.port}"
        self.login()

    def login(self):
        """Login to superset"""
        login_url = f"{self.url}/login/"
        login_payload = {"username": self.username, "password": self.password}

        # Perform login
        response = self.session.post(login_url, data=login_payload)

        if response.status_code != 200:
            logging.info("Successfully connected to superset")

            raise ConnectionError(
                f"Failed to authenticate with Superset API. Status code: {response.status_code}"
            )
            
    def import_dashboard(self, path_to_zip):
        """Imports dashboard from zipfile"""
        import_url = f"{self.url}/api/v1/dashboard/import/"
        
                # Prepare the authentication data
        auth = (self.username, self.password)

        # Prepare the file to be uploaded
        files = {
            'formData': ('dashboard.zip', open(path_to_zip, 'rb'), 'application/zip')
        }

        # Prepare additional form data
        form_data = {
            'overwrite': 'true'  # You can adjust this as needed
        }

        response = self.session.post(import_url, auth=auth, data=form_data, files=files)

        if response.status_code != 200:
            logging.info("Successfully imported a dashboard to superset")
        

    def close(self):
        """Closes a session"""
        self.session.close()
