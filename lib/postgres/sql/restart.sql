-- Drop the schema if it exists
DROP SCHEMA IF EXISTS my_finances CASCADE;

-- Create the schema
CREATE SCHEMA my_finances;

-- Raw data history for checking
create table "my_finances"."raw_historical_checking" (
    date date
    , amount numeric(18, 2)
    , nothing text
    , nothing2 text
    , description varchar(600)
);

-- Raw data history for savings
create table "my_finances"."raw_historical_savings" (
    date date
    , amount numeric(18, 2)
    , nothing text
    , nothing2 text
    , description varchar(600)
);

-- Raw data history for credit
create table "my_finances"."raw_historical_credit" (
    "Status" varchar(150)
    , "Date" date
    , "Description" varchar(600)
    , "Debit" numeric(18, 2)
    , "Credit" numeric(18, 2)
    , "Member Name" varchar(150)
);