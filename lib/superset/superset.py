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

        if response.status_code == 200:
            logging.info("Successfully connected to superset")
        else:
            raise ConnectionError(
                f"Failed to authenticate with Superset API. Status code: {response.status_code}"
            )

    def set_csrf_token(self):
        """Get token to auth"""
        security_url = f"{self.url}/api/v1/security/csrf_token/"
        headers = {
            "Authorization": f"Bearer {self.get_superset_access_token()}",
            "Accept": "application/json",
        }
        response = self.session.get(security_url, headers=headers)

        return str(response.json()["result"])

    def get_dashboards(self):
        """Get dashboards"""
        dashboard_url = f"{self.url}/api/v1/dashboard/"
        login_payload = {
            "username": self.username,
            "password": self.password,
            "provider": "db",
        }

        # Make the POST request
        response = self.session.get(dashboard_url, data=login_payload)

        print(response.status_code)
        print(response.json)

    def get_superset_access_token(self):
        """Authenticate and get access token"""
        response = self.session.post(
            "%s/api/v1/security/login" % self.url,
            json={
                "username": self.username,
                "password": self.password,
                "provider": "db",
                "refresh": True,
            },
        )
        access_token = response.json()["access_token"]
        print("Received access token.")
        return access_token

    # Function to import dashboard from a zip file
    def import_dashboard(self, path_to_zip):
        """hello"""
        with open(path_to_zip, "rb") as file:
            files = {
                "formData": (
                    "lib/superset/resources/personal_finance_test_dashboard.zip",
                    file,
                    "application/zip",
                )
            }
            headers = {
                "X-CSRFToken": self.set_csrf_token(),
                "Authorization": f"Bearer {self.get_superset_access_token()}",
                "accept": "application/json",
                "Referer": f"{self.url}/api/v1/dashboard/import/",
            }
            response = self.session.post(
                f"{self.url}/api/v1/dashboard/import/", headers=headers, files=files
            )

            if response.status_code != 200:
                raise Exception(f"Failed to import dashboard: {response.text}")
            print("success")

    # def import_dashboard(self, path_to_zip):
    #     """Imports dashboard from zipfile"""
    #     import_url = f"{self.url}/api/v1/dashboard/import/"

    #     # Define your custom headers
    #     new_headers = {
    #         "accept": "application/json",
    #         "overwrite": "true",
    #         "passwords": "postgres",
    #         "X-CSRFToken": self.csrf_token

    #     }

    #     try:

    #         # Prepare the file for upload
    #         files = {
    #             'formData': (
    #                 path_to_zip,
    #                 open(path_to_zip, 'rb'),
    #                 'application/json'
    #             )
    #         }

    #         # Make the POST request
    #         response = self.session.post(import_url, headers = new_headers, files = files)

    #         if response.status_code == 200:
    #             print("Successfully imported a dashboard to superset")

    #         print(response.status_code)
    #         print(self.csrf_token)
    #     except Exception as err:
    #         print("error")
    #         print(err)

    def close(self):
        """Closes a session"""
        self.session.close()
