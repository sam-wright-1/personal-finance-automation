drop table if exists personal_finance.my_finances.sum_category;

create table personal_finance.my_finances.sum_category
as

select 

SUM(amount) as total
, transaction_category
, month
, year

from personal_finance.my_finances.categories
group by 
    month
    , year
    , transaction_category;

