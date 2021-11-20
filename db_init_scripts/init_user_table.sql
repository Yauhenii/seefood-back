CREATE TABLE IF NOT EXISTS seefood.user(
    id serial PRIMARY KEY,
    login_name varchar(50) UNIQUE,
    full_name varchar(50) NOT NULL,
    address_name varchar(200) NOT NULL,
    phone_number varchar(15) NOT NULL
);