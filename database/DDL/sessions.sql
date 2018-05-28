create table sessions (
        user_id integer references users(id),
        session varchar(500) not null,
        expire_time timestamp not null,
        creation_time timestamp NOT NULL,
        PRIMARY KEY(user_id)
);