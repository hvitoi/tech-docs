DROP TABLE table_name;

/* IF EXISTS */
DROP TABLE IF EXISTS table_name;

/* CASCADE */
-- Drop even if it has dependencies
DROP TABLE table_name CASCADE;

/* EXAMPLES */
-- Restrict does not delete the table if any object depends on it. It's the deafult option!
DROP TABLE test RESTRICT;

-- Delete the table even if it has dependencies
DROP TABLE test CASCADE;