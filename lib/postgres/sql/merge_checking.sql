merge into
    "personal_finance"."my_finances"."raw_historical_checking" as historical
using
    (select
        date::date
        , amount::numeric(18, 2)
        , description::varchar(600)
    from "personal_finance"."my_finances"."raw_checking") as raw_data
    on historical.date = raw_data.date
        and historical.amount = raw_data.amount
        and historical.description = raw_data.description
when matched then
    update set 
        date = raw_data.date
        , amount = raw_data.amount
        , description = raw_data.description
when not matched then
    insert (date, amount, description)
    values (raw_data.date, raw_data.amount, raw_data.description);
