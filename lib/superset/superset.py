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
        (
            self.auth_token,
            self.refresh_token,
        ) = self.__get_superset_access_and_refresh_tokens()
        self.csrf_token = self.__set_csrf_token()

    def __set_csrf_token(self):
        """Get token to auth"""
        security_url = f"{self.url}/api/v1/security/csrf_token/"
        headers = {
            "Authorization": f"Bearer {self.auth_token}",
            "Accept": "application/json",
            "Connection": "keep-alive",
        }
        response = self.session.get(security_url, headers=headers)

        return str(response.json()["result"])

    def __get_superset_access_and_refresh_tokens(self):
        """Authenticate and get access token"""
        access_token_url = f"{self.url}/api/v1/security/login"

        json_headers = {
            "username": self.username,
            "password": self.password,
            "provider": "db",
            "refresh": True,
        }

        response = self.session.post(access_token_url, json=json_headers)

        if response.status_code == 200:
            logging.info("Successfully connected to superset")
        else:
            raise ConnectionError(
                f"Failed to authenticate with Superset API. Status code: {response.status_code}"
            )
        access_token = response.json()["access_token"]
        refresh_token = response.json()["refresh_token"]

        return access_token, refresh_token

    def star_things(self):
        """Imports dashboard from zipfile"""
        star_url = f"{self.url}/api/v1/dashboard/10/favorites/"

        # Define your custom headers
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.auth_token}",
            "X-CSRFToken": self.csrf_token,
            "Referer": f"{self.url}/api/v1/security/csrf_token/",
        }

        response = self.session.post(star_url, headers=headers)

        if response.status_code == 200:
            print("Favorited something")

        print(response.status_code)

    def favorite_status(self):
        """Imports dashboard from zipfile"""
        star_url = f"{self.url}/api/v1/dashboard/favorite_status/"

        # Define your custom headers
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.auth_token}",
            "X-CSRFToken": self.csrf_token,
        }

        response = self.session.get(star_url, headers=headers)

        if response.status_code == 200:
            print("Favorited something")

        print(response.status_code)
        print(response.json())

    def import_dashboard(self, path_to_zip):
        """Imports dashboard from zipfile"""
        import_dashboard_url = f"{self.url}/api/v1/dashboard/import/"

        # Define your custom headers
        import_headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.auth_token}",
            "X-CSRFToken": self.csrf_token,
        }
        import_form = {
            "overwrite": True,
            "formData": (
                "@personal_finance_test_dashboard.zip;type=application/x-zip-compressed"
            ),
        }
        # Make the POST request
        response = self.session.post(
            import_dashboard_url, headers=import_headers, files=import_form
        )

        if response.status_code == 200:
            print("Successfully imported a dashboard to superset")

        print(response.status_code)

    def get_dashboards(self):
        """Get all dashboard json"""
        dashboard_url = f"{self.url}/api/v1/dashboard/"
        headers = {
            "Accept": "application/json",
            "Authorization": f"Bearer {self.auth_token}",
            "X-CSRFToken": self.csrf_token,
        }

        response = self.session.get(dashboard_url, headers=headers)

        return response.json()

    def close(self):
        """Closes a session"""
        self.session.close()

