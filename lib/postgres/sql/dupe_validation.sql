drop table if exists personal_finance.my_finances.dupe_validation;

create table personal_finance.my_finances.dupe_validation
as
select
    date,
    amount,
    type,
    individual,
    transaction_category,
    description,
    COUNT(*) as total_rows

from personal_finance.my_finances.categories

group by
    1, 2, 3, 4, 5, 6
