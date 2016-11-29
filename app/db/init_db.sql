create table users (
    id serial not null,
    username varchar(64),
    password varchar(255),
    email varchar(128),
    date_confirmed timestamp without time zone,
    role smallint,
    status smallint,
    constraint users_pkey primary key (id)
);

create table posts (
    id serial not null,
    title varchar(128),
    body varchar(256),
    date_created timestamp without time zone,
    user_id integer not null,
    CONSTRAINT posts_user_id_fkey FOREIGN KEY (user_id)
      REFERENCES users (id) MATCH SIMPLE
      ON UPDATE NO ACTION ON DELETE NO ACTION
);