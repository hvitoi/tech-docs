CREATE TABLE person (id serial PRIMARY KEY, is_cool Boolean);

CREATE INDEX ix_person_is_cool ON person(is_cool);

-- Indexing on creation
CREATE TABLE person (
  id INT NOT NULL,
  last_name TEXT NOT NULL,
  first_name TEXT NOT NULL,
  PRIMARY KEY (id),
  INDEX name (last_name, first_name)
);
