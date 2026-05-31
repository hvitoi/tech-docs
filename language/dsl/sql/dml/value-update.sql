/* UPDATE */ 
UPDATE table_name
SET
column_name = 'new_value';



/* EXAMPLES */
UPDATE link
SET description = 'Empty Description'; -- All the rows from the column 'description' receives 'Empty Description'
--
UPDATE link
SET description = 'Name starts with G'
WHERE name LIKE 'G%';
--
UPDATE link
SET description = name; -- values from 'description' receive values from 'name'
--
UPDATE link
SET description = 'New descriptions'
WHERE id IN (1, 3, 5)
RETURNING id, url, name, description; -- Returns columns of the rows affected
--
UPDATE shirt
SET color='off white', shirt_size='XS'
WHERE color='white';
