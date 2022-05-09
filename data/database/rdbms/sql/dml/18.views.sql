--
CREATE VIEW customer_info AS
SELECT
  first_name,
  last_name,
  email,
  address,
  phone
FROM
  customer
  JOIN address ON customer.address_id = address.address_id;

--
ALTER VIEW customer_info RENAME TO customer_master_list;

--
SELECT
  *
FROM
  customer_master_list;

-- 
DROP VIEW IF EXISTS customer_master_list;

--
CREATE
OR REPLACE VIEW view_name AS
SELECT
  *
FROM
  table
where
  id = 1