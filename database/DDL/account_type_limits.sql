create table account_type_limits(
        id serial unique not null,
        account_type_limit_name char(50) not null
        max_value integer not null
);