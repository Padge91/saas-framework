create table users (
        id serial unique not null,
        username char(20) not null,
        email char(50) not null,
        password char(200) not null,
        salt char(200) not null,
        creation_date timestamp not null,
        modified_date timestamp not null,
        active boolean not null,
        primary key (id)
);