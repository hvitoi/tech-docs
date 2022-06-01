/* NOT NULL CONSTRAINT */
CREATE TABLE learn_null (
	first_name VARCHAR(50),
	sales integer NOT NULL -- Does not insert record passing only value for first_name
);
--
INSERT INTO learn_null(first_name, sales)
VALUES ('John', 50)
RETURNING *;