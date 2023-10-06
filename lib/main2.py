from scripts.postgres_sql import run_sql_statements
# from scripts.docker_run_sql import run_sql

def main():
    """Run processes"""    
    try:
        # Takes imports, transforms imports, takes google sheets existing data, dedups
        google_sheets_upload()
        
        # Runs airbyte sync between google sheets and postgres
        airbyte()
        
        # Runs sql statements in the postgres container
        run_sql_statements()
        
        print("Process Completed")
        
    except Exception as err:
        print("Something went wrong", err)

if __name__ == "__main__":
    main()
