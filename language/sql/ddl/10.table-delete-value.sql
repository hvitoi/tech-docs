/* DELETE */
DELETE FROM table_name
WHERE column = 'value'



/* EXAMPLES */
DELETE FROM link
WHERE name LIKE 'B%' -- Delete entries starting with B
RETURNING *; -- Return all the columns from the deleted entries
--
DELETE FROM cat
WHERE name='Momo';
--
DELETE FROM cat; -- Delete everything in the table