CREATE TABLE "my_table" (
  "id" serial PRIMARY KEY,
  "is_cool" Boolean
);

CREATE INDEX "by_is_cool"
ON my_table(is_cool);


-- Indexing on creation
CREATE TABLE "my_table" (
  "id" INT NOT NULL,
  "last_name" CHAR(30) NOT NULL,
  "first_name" CHAR(30) NOT NULL,
  PRIMARY KEY (id),
  INDEX name (last_name, first_name)
);
