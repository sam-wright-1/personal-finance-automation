-- Connect to the database
\c personal_finance;

-- Create a schema within the database
create schema my_finances;

-- Raw data history for checking
create table "personal_finance"."my_finances"."raw_historical_checking" (
    date date
    , amount numeric(18, 2)
    , nothing text
    , nothing2 text
    , description varchar(600)
);

-- Raw data history for savings
create table "personal_finance"."my_finances"."raw_historical_savings" (
    date date
    , amount numeric(18, 2)
    , nothing text
    , nothing2 text
    , description varchar(600)
);

-- Raw data history for credit
create table "personal_finance"."my_finances"."raw_historical_credit" (
    "Status" varchar(150)
    , "Date" date
    , "Description" varchar(600)
    , "Debit" numeric(18, 2)
    , "Credit" numeric(18, 2)
    , "Member Name" varchar(150)
);