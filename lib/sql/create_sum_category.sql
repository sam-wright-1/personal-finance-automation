drop table if exists finance.sum_category;

create table finance.sum_category
as

select 

SUM(amount) as total
, transaction_category
, month
, year

from finance.categories
group by 
    month
    , year
    , transaction_category;

