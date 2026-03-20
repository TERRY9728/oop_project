CREATE TABLE IF NOT EXISTS users (
    id_num INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    borrowed_book TEXT DEFAULT ""
);

CREATE TABLE IF NOT EXISTS books (
    id_num INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    author TEXT,
    stock INTEGER CHECK (stock >= 0)
);

CREATE TABLE IF NOT EXISTS librarians (
    id_num INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);
