create table account_types(
        id serial UNIQUE not null,
        type_name char(50) not null
);