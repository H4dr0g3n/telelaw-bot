CREATE TABLE articles
(
    id             SERIAL PRIMARY KEY,
    laws_name      VARCHAR(255) NOT NULL,
    article_number VARCHAR(255)  NOT NULL,
    title          VARCHAR(255),
    text           TEXT,
    last_modified  DATE
);