"""Airbyte Class"""

import base64
import logging
import os
import time

import requests


class Airbyte:
    """Class for airbyte connection"""

    def __init__(self):
        self.host = os.environ["AIRBYTE_HOST"]
        self.username = os.environ["AIRBYTE_USER"]
        self.password = os.environ["AIRBYTE_PASSWORD"]
        self.header = self.set_header()
        self.payload = self.set_payload()

    def set_header(self):
        """Header info"""
        sample_string = self.username + ":" + self.password
        sample_string_bytes = sample_string.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")

        auth = "Basic " + base64_string

        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": auth,
        }

        return headers

    def set_payload(self):
        """Setting Payload"""

        payload = {
            "jobType": "sync",
            "connectionId": "",
        }
        return payload

    def connect(self, username, password):
        """Connect to Airbyte"""

    def construct_header(self):
        """Set Header"""

    def trigger_sync(self):
        """Trigger job sync"""
        url = f"http://{self.host}:8000/api/v1/connections/sync"

        airbyte_request = requests.post(url, json=self.payload, headers=self.header)

        if airbyte_request.status_code == 200:
            logging.info("Data replication started")
            url = "https://api.airbyte.com/v1/jobs/jobId"
            logging.info("Done")
        else:
            print("Refresh Failed")

    def get_sync_status(self, job_id):
        """Get job sync status"""

        url = f"https://api.airbyte.com/v1/jobs/{job_id}"

        while ready == False:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return True
            else:
                time.sleep(3)

    def list_connections(self):
        """Get connection list"""
        url = (
            f"http://{host}:8000/v1/connections?includeDeleted=false&limit=20&offset=0"
        )

        try:
            response = requests.get(url, headers=self.headers)
            if response.status_code == 200:
                return response
            else:
                return "Bad Response"
        except:
            logging.info("Something went wrong")

    def list_sources(self):
        """Get source list"""
        pass

    def list_destinations(self):
        """Get destination list"""
        pass


# def airbyte():
#     """Generate airbyte sync"""
#     url = "http://airbyte-proxy:8000/api/v1/connections/sync"

#     sample_string = "airbyte:password"
#     sample_string_bytes = sample_string.encode("ascii")

#     base64_bytes = base64.b64encode(sample_string_bytes)
#     base64_string = base64_bytes.decode("ascii")

#     auth = "Basic " + base64_string

#     payload = {
#         "jobType": "sync",
#         "connectionId": "",
#     }
#     headers = {
#         "accept": "application/json",
#         "content-type": "application/json",
#         "Authorization": auth,
#     }

#     airbyte_request = requests.post(url, json=payload, headers=headers)

#     if airbyte_request.status_code == 200:
#         print("Data replication started")
#         time.sleep(15)
#         print("Done")
#     else:
#         print("Refresh Failed")
