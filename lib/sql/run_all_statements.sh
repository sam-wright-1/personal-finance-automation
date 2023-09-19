#!/bin/bash

# PostgreSQL server information
DB_HOST="localhost"
DB_PORT="5432"
DB_NAME="finance"
DB_USER="postgres"
DB_PASSWORD="postgres"

# SQL query to execute
CATEGORIES="sql/create_categories.sql"
SUM_CATEGORIES="sql/create_sum_category.sql"
MASTER_JOIN="sql/create_master_join.sql"

# Run psql command
psql -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -U "$DB_USER" -f "$MASTER_JOIN"
psql -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -U "$DB_USER" -f "$CATEGORIES"
psql -h "$DB_HOST" -p "$DB_PORT" -d "$DB_NAME" -U "$DB_USER" -f "$SUM_CATEGORIES"