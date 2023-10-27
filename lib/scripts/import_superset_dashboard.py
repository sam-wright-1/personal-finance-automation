from lib.superset.superset import Superset

superset_connection = Superset()


superset_connection.import_dashboard('lib/superset/resources/personal_finance_test_dashboard.zip',)


superset_connection.close()