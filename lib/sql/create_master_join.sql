drop table if exists public.master_join;

create table public.master_join
as
SELECT 
    "Type" as type
    , "Date" as date
    , cast(Amount as decimal) as amount
    , Description as description
    , Individual as individual
    , cast("Month" as int) as month
    , cast("Year" as int) as year
    , "Day" as day
    , Flow as flow

FROM public."raw_data_2021"

UNION ALL -- 2021 has 2 duplicate rows (both airline tickets)

SELECT 
    "Type" as type
    , "Date" as date
    , cast(Amount as decimal) as amount
    , Description as description
    , Individual as individual
    , cast("Month" as int) as month
    , cast("Year" as int) as year
    , "Day" as day
    , Flow as flow

FROM public."raw_data_2022"

UNION ALL

SELECT 
    "Type" as type
    , "Date" as date
    , cast(Amount as decimal) as amount
    , Description as description
    , Individual as individual
    , cast("Month" as int) as month
    , cast("Year" as int) as year
    , "Day" as day
    , Flow as flow

FROM public."raw_data_2023";