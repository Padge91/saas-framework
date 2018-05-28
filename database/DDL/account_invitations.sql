create table account_invitations(
        account_id integer references accounts(id),
        user_id integer references(users(id),
        invite_date timestamp not null,
        invite_code char(500) not null
);