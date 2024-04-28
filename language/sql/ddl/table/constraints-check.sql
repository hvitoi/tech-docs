/* CHECK CONSTRAINT */
CREATE TABLE users (
	id SERIAL PRIMARY KEY,
	first_name VARCHAR(50),
	birth_date DATE CHECK(birth_date > '1900-01-01'),
	join_date DATE CHECK(join_date > birth_date),
	salary INTEGER CHECK(salary>0) -- Salary - 10 cannot be inserted
);
--
INSERT INTO users(first_name, birth_date,join_date, salary)
VALUES
('Joe', '1980-02-02', '1990-04-04', 10),
('Maria', '1977-03-22', '2020-02-02', 20); -- Salary -10 cannot be inserted!
--
CREATE TABLE checktest (
	sales INTEGER CONSTRAINT positive_salves CHECK(sales>0) -- Give a name to the check constraint. In the error appears the violate the constraint "positive_sales"
);
--
INSERT INTO checktest(sales)
VALUES (10);