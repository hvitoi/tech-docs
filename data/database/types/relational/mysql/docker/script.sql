CREATE DATABASE IF NOT EXISTS facebook;
USE facebook;

CREATE TABLE IF NOT EXISTS user
(
    id INT NOT NULL AUTO_INCREMENT,
    name TEXT,
    phone TEXT,
    PRIMARY KEY (id)
);

INSERT INTO user (name, phone) 
VALUES
('Maria','1234'),
('Joao','431'),
('Jose','4315'),
('Leopoldo','6453'),
('Telma','65463');
