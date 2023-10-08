CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    username TEXT UNIQUE,
    password TEXT,
    role TEXT
);
CREATE TABLE areas (
    id SERIAL PRIMARY KEY,
    name TEXT,
    thread_count INTEGER DEFAULT 0,
    message_count INTEGER DEFAULT 0,
    last_message_time TIMESTAMP
);
CREATE TABLE threads (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    area_id INTEGER REFERENCES areas(id),
    sent_at TIMESTAMP
);
CREATE TABLE messages (
    id SERIAL PRIMARY KEY,
    title TEXT,
    content TEXT,
    user_id INTEGER REFERENCES users(id),
    thread_id INTEGER REFERENCES threads(id),
    sent_at TIMESTAMP
);

