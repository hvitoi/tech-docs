INSERT INTO
    cat (name, age)
VALUES
    ('Momo', 12),
    ('Jingi', 3);

--
INSERT INTO
    cat () -- Insert empty row
VALUES
    ();

-- Insert rows from another table
-- The id from the old table will be copied
INSERT INTO
    cat_copy
SELECT
    *
FROM
    cat
WHERE
    name = 'Bing';
