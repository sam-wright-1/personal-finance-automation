"""Runs all of the code from your local machine (not inside the container)"""

from lib.airbyte.airbyte import Airbyte
from lib.postgres.postgres import Postgres

Airbyte()

Postgres()
