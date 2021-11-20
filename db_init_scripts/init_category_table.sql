CREATE TABLE IF NOT EXISTS seefood.category(
    id serial PRIMARY KEY,
    category_name varchar(50) UNIQUE,
    avg_calories numeric(10,3) NOT NULL
);