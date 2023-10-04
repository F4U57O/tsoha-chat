CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT
);
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    user_id INTEGER REFERENCES users(id),
    thread_id INTEGER REFERENCES threads(id),
    sent_at TIMESTAMP
);
CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    area_id INTEGER REFERENCES areas(id),
    sent_at TIMESTAMP
);
CREATE TABLE areas (
    id SERIAL PRIMARY KEY,
    name TEXT
);
