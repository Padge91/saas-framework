create table service_tickets(
        id serial UNIQUE not null,
        owner integer references users(id),
        creation_date timestamp not null,
        ticket_content char(2000) not null,
        resolved boolean not null,
        PRIMARY KEY(id)
);