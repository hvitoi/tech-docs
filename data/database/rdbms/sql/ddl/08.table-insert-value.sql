/* INSERT VALUES */
INSERT INTO table_name (field1, field2)
VALUES
(value1, value2),
(value1, value2);

INSERT INTO table_name -- Insert only one record
SET field1 = value1,
    field2 = value2;



/* EXAMPLES */

INSERT INTO cat (age, name)
VALUES
(12, 'Momo'),
(3, 'Jingi');
--
INSERT INTO link (url, name)
VALUES 
    ('www.bing.com', 'Bing'),
    ('www.yahoo.com', 'Yahoo');
--
INSERT INTO cat ()      -- Insert empty row
VALUES ();
--
INSERT INTO link_copy -- Insert rows from another table
    SELECT * FROM link
    WHERE name='Bing'; -- The id from the old table will be copied