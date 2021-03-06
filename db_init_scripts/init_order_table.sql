CREATE TABLE IF NOT EXISTS seefood.order(
    id SERIAL PRIMARY KEY,
    owner_id int NOT NULL REFERENCES seefood.user(id) ON DELETE CASCADE,
    food_name varchar(200) NOT NULL,
    category_id int NOT NULL REFERENCES seefood.category(id) ON DELETE CASCADE,
    price decimal(10,2) NOT NULL,
    due_date date NOT NULL,
    comment varchar(500) NOT NULL,
    is_anonymus boolean NOT NULL,
    is_completed boolean NOT NULL,
    is_trashed boolean NOT NULL
);