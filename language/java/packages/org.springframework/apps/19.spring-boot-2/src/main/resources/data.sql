INSERT INTO
  user
VALUES
  (10001, SYSDATE(), 'AB'),
  (10002, SYSDATE(), 'Jill'),
  (10003, SYSDATE(), 'Jam');

INSERT INTO
  post
VALUES
  (11001, 'My First Post', 10001),
  (11002, 'My Second Post', 10001);