create table accounts(
        id serial UNIQUE not null,
        account_name char(200) not null,
        creation_date timestamp not null,
        account_type_id integer references account_types(id),
        owner_id integer references users(id)
);