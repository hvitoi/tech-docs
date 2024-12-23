DROP DATABASE IF EXISTS join_us;
CREATE DATABASE join_us;
USE join_us;

CREATE TABLE user (
  id INTEGER AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255),
  email VARCHAR(255) UNIQUE,
  created_at TIMESTAMP DEFAULT NOW()
);

INSERT INTO user (name, email)
VALUES('Katie', 'Katie34@yahoo.com'), ('Tunde', 'Tunde@gmail.com');