/* UNIQUE CONSTRAINT */
CREATE TABLE people (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(50),
	email VARCHAR(100) UNIQUE -- Duplicate key value violates unique constraints
);
--
INSERT INTO people (id, first_name, email)
VALUES
(1, 'Joe', 'joe@gmail.com'),
(2, 'Joseph', 'joseph@gmail.com');

SELECT * FROM people