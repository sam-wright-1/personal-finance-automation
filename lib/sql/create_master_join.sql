drop table if exists finance.master_join;

create table finance.master_join
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

FROM finance."2021_RT"

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

FROM finance."2022_RT"

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

FROM finance."2023_RT";