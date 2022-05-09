
/* ALTER TABLE */ 

ALTER TABLE table_name 
ADD COLUMN column_name data_type,
DROP COLUMN column_name,
RENAME COLUMN old_name TO new_name,
RENAME TO new_table_name;  -- Changes the name of the table itself



/* EXAMPLES */
--
ALTER TABLE cat 
ADD COLUMN weight int,
DROP COLUMN nickname,
RENAME COLUMN name TO cat_name,
RENAME TO lovely_cat;

/* EXAMPLES */
--
ALTER TABLE dog 
AUTO_INCREMENT=3000 -- all the new entries now start at 3000