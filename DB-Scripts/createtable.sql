DROP Table account;

CREATE TABLE account (
    user_id serial Primary Key,
    username varchar(30) Unique Not NUll,
    password varchar(30) Not Null
);