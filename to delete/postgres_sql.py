import os

import psycopg2

# Database connection parameters
db_params = {
    "host": "finance_automation_database",
    "user": "postgres",
    "password": "postgres",
    "dbname": "personal_finance",
}

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sql_scripts = [
    "create_master_join.sql",
    "create_categories.sql",
    "create_sum_category.sql",
]


def run_sql_statements():
    """Running sql statements with psychopg2"""

    # Establish a database connection
    conn = psycopg2.connect(**db_params)

    # Create a cursor
    cur = conn.cursor()

    # Loop through each script file and execute its contents
    for script_file in sql_scripts:
        script_path = os.path.join(parent_dir, "sql", script_file)
        with open(script_path, "r") as sql_file:
            sql_commands = sql_file.read()

        try:
            cur.execute(sql_commands)

            conn.commit()  # Commit after each script execution

            print(
                f"Table {script_file.replace('create_', '').replace('.sql', '')} created"
            )

        except psycopg2.DatabaseError as err:
            conn.rollback()
            print("Error creating table:", err)

    # Close the cursor and connection
    cur.close()
    conn.close()
