drop table if exists "personal_finance"."my_finances"."transformed_historical";
-- Combination of all sources transformed
create table "personal_finance"."my_finances"."transformed_historical" 
as
(
    select 
        'CREDIT' as type
        , "Date" as date
        , case 
            when "Debit" is NULL
            then "Credit"
            else "Debit"
        end as amount
        , "Description" as description
        , "Member Name" as individual
        , extract(day from "Date") as day
        , extract(month from "Date") as month
        , extract(year from "Date") as year
        , case
            when "Debit" is not null then 'OUT'
            else 'IN' 
        end as flow
    from 
        "personal_finance"."my_finances"."raw_historical_credit"

    UNION ALL 

    select 
        'CHECKING' as type
        , date as date
        , amount as amount
        , description as description
        , NULL as individual
        , extract(day from date) as day
        , extract(month from date) as month
        , extract(year from date) as year
        , case
            when amount >= 0 then 'IN'
            else 'OUT' 
        end as flow
    from 
        "personal_finance"."my_finances"."raw_historical_checking"

    UNION ALL 

    select 
        'SAVINGS' as type
        , date as date
        , amount as amount
        , description as description
        , NULL as individual
        , extract(day from date) as day
        , extract(month from date) as month
        , extract(year from date) as year
        , case
            when amount >= 0 then 'IN'
            else 'OUT' 
        end as flow
    from 
        "personal_finance"."my_finances"."raw_historical_savings"
);