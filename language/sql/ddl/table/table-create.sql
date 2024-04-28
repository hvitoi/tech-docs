/* Create table */
CREATE TABLE IF NOT EXISTS `user`
(
  `id` int(11) NOT NULL AUTO_INCREMENT, -- Use INT NOT NULL AUTO_INCREMENT for primary keys
  `user_detail_id` int(11) DEFAULT NULL,
  `first_name` varchar(45) DEFAULT NULL,
  `last_name` varchar(45) DEFAULT NULL,
  `email` varchar(45) DEFAULT NULL,
  `description` varchar(100) DEFAULT `no description`
  
  PRIMARY KEY (`id`) -- Primary keys are UNIQUE and NOT NULL
  FOREIGN KEY(`user_detail_id`) REFERENCES `user_detail`(`id`) ON DELETE CASCADE -- Delete records from the related table when deleted from this table -- ON DELETE NO ACTION ON UPDATE NO ACTION
);

/* Create new table copied from another table */
CREATE TABLE IF NOT EXISTS `new_table` (LIKE `old_table`); -- Copy the structure, but not the values
CREATE TABLE IF NOT EXISTS `new_table` AS (SELECT * FROM `old_table`); -- Copy structure and values

-------------------------

/* EXAMPLES */

-- Cat
CREATE TABLE `cat`(
  `name` VARCHAR(100),
  `age` INT
);
CREATE TABLE `cat2`(
  `name` VARCHAR(100) DEFAULT "kitten", -- default value is given if no name is provided
  `age` INT DEFAULT 99
)
CREATE TABLE `cat3`(
  `id` INT AUTO_INCREMENT,
  `name` varchar(100),
  `age` int,
  PRIMARY KEY (id)  -- PK
);

-- Customer and Order (PK + FK)
CREATE TABLE `customers`(
    `id` INT AUTO_INCREMENT PRIMARY KEY,  -- PK
    `first_name` VARCHAR(100),
    `last_name` VARCHAR(100),
    `email` VARCHAR(100)
);
CREATE TABLE `orders`(
  `id` INT AUTO_INCREMENT PRIMARY KEY,  -- PK
  `order_date` DATE,
  `amount` DECIMAL(8,2),
  `customer_id` INT,  -- values inserted here are validated -> must match with any id in customer table
  FOREIGN KEY(`customer_id`) 
    REFERENCES `customers`(`id`)   -- FK ensures that records with no reference to the parent table are NOT inserted
    ON DELETE CASCADE  --Records in this table automatically gets delete when delete from parent table
);

-- Accounts
CREATE TABLE IF NOT EXISTS `account` (
	`user_id` SERIAL PRIMARY KEY,
	`username` VARCHAR(50) UNIQUE NOT NULL,
	`password` VARCHAR(50) NOT NULL,
	`email` VARCHAR(355) UNIQUE NOT NULL,
	`created_on` TIMESTAMP NOT NULL,
	`last_login` TIMESTAMP
);
CREATE TABLE `account_role` (
	`user_id` INTEGER NOT NULL,
	`role_id` INTEGER NOT NULL,
	`grant_date` TIMESTAMP WITHOUT TIME ZONE,
	PRIMARY KEY (`user_id`, `role_id`),
	
	CONSTRAINT `account_role_role_id_fkey` FOREIGN KEY (`role_id`)
		REFERENCES role (`role_id`) MATCH SIMPLE
		ON UPDATE NO ACTION ON DELETE NO ACTION,
	CONSTRAINT `account_role_user_id_fkey` FOREIGN KEY (`user_id`)
		REFERENCES `account` (`user_id`) MATCH SIMPLE
		ON UPDATE NO ACTION ON DELETE NO ACTION
);
