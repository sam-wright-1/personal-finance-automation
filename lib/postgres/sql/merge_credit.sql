merge into
    "personal_finance"."my_finances"."raw_historical_credit" as historical
using
    (select
        "Status"::varchar(150)
        , "Date"::date
        , "Description"::varchar(600)
        , case
            when "Debit"::numeric(18, 2) is null
            then 0
            else "Debit"::numeric(18, 2)
        end as "Debit"
        , case
            when "Credit"::numeric(18, 2) is null
            then 0
            else "Credit"::numeric(18, 2)
        end as "Credit"
        , "Member Name"::varchar(150)
    from "personal_finance"."my_finances"."raw_credit") as raw_data
    on historical."Status" = raw_data."Status"
        and historical."Date" = raw_data."Date"
        and historical."Description" = raw_data."Description"
        and historical."Debit" = raw_data."Debit"
        and historical."Credit" = raw_data."Credit"
        and historical."Member Name" = raw_data."Member Name"
when matched then
    update set 
        "Status" = raw_data."Status"
        , "Date" = raw_data."Date"
        , "Description" = raw_data."Description"
        , "Debit" = raw_data."Debit"
        , "Credit" = raw_data."Credit"
        , "Member Name" = raw_data."Member Name"
when not matched then
    insert ("Status", "Date", "Description","Debit", "Credit", "Member Name")
    values (raw_data."Status", raw_data."Date", raw_data."Description", raw_data."Debit", raw_data."Credit", raw_data."Member Name");