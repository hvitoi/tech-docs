/* SHOW TRIGGERS */
SHOW TRIGGERS;

/* DROP TRIGGER */
DROP TRIGGER trigger_name;



/* INSERT TRIGGERS*/
-- BEFORE

-- Prevent underaged user
DELIMITER $$ -- The new ; is now $$
CREATE TRIGGER must_be_adult -- Trigger name
  BEFORE INSERT ON user FOR EACH ROW -- Run every time before a user is inserted
  BEGIN
    IF NEW.age < 18 -- NEW reffers to the new user being inserted
      THEN
        SIGNAL SQLSTATE '45000' -- SQL State error. Generic error: Unhandled user-defined exception
        SET MESSAGE_TEXT = 'Must be an adult!'; -- message_text is to message to be display as error
    END IF;
  END;
$$
DELIMITER ; -- Change back the delimiter to ;

-- Prevent self-follow
DELIMITER $$
CREATE TRIGGER cannot_follow_self
  BEFORE INSERT ON follows FOR EACH ROW
  BEGIN
    IF NEW.follower_id = NEW.followee_id
    THEN
      SIGNAL SQLSTATE '45000'
      SET MESSAGE_TEXT = 'Cannot follow yourself!';
    END IF;
  END;
$$
DELIMITER ;


-- AFTER

-- Logging when user has unfollowed another user
DELIMITER $$
CREATE TRIGGER create_unfollow
  AFTER DELETE ON follows FOR EACH ROW -- Only triggers if the data is successfully deleted
  BEGIN
    INSERT INTO unfollows
      SET follower_id = OLD.follower_id,  -- OLD reffers to the deleted record
          followee_id = OLD.followee_id;
  END$$
DELIMITER ;
