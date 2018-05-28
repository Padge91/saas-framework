create table password_resets(
        user_id integer references users(id),
        reset_secret varchar(500) not null,
        reset_expire timestamp not null
);