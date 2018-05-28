create table account_members(
        account_id integer references accounts(id),
        user_id integer references users(id)
);