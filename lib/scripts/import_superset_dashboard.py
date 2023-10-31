"""Import Superset Dashboard"""

from lib.superset.superset import Superset

superset_connection = Superset()

print(superset_connection.star_things())
# superset_connection.favorite_status()


# superset_connection.import_dashboard(
#     "lib/superset/resources/personal_finance_test_dashboard.zip",
# )


# print(superset_connection.get_dashboards())

superset_connection.close()
