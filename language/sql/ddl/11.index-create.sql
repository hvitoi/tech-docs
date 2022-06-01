-- creates an index with id (pk) + name
CREATE INDEX employees_name ON empoyees(name);

-- indexes are matched for literal values - LIKE operators wont consult index