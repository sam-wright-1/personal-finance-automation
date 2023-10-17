drop table if exists personal_finance.my_finances.dupe_validation;

create table personal_finance.my_finances.dupe_validation
as
SELECT 
    date
    , amount
    , type
    , individual
    , transaction_category
    , description
    , COUNT(1) as total_rows

FROM personal_finance.my_finances.categories

GROUP BY 
    1,2,3,4,5,6