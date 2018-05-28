create table account_type_limit_instances(
        account_id integer references accounts(id),
        account_type_limit_id integer references account_type_limit(id),
        current_value integer not null
);