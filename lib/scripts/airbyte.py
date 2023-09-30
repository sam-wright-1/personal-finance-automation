import time
import base64
import requests


def airbyte():
    """Generate airbyte sync"""
    url = "http://airbyte-proxy:8000/api/v1/connections/sync"

    sample_string = "airbyte:password"
    sample_string_bytes = sample_string.encode("ascii")

    base64_bytes = base64.b64encode(sample_string_bytes)
    base64_string = base64_bytes.decode("ascii")

    auth = "Basic " + base64_string

    payload = {
        "jobType": "sync",
        "connectionId": "",
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "Authorization": auth,
    }

    airbyte_request = requests.post(url, json=payload, headers=headers)

    if airbyte_request.status_code == 200:
        print("Refresh Running")
        time.sleep(15)
    else:
        print("Refresh Failed")