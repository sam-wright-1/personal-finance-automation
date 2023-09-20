drop table if exists public.sum_category;

create table public.sum_category
as

select 

SUM(amount) as total
, transaction_category
, month
, year

from public.categories
group by 
    month
    , year
    , transaction_category;

