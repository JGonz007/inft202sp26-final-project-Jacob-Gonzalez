DROP TABLE IF EXISTS people;
DROP TABLE IF EXISTS department;

CREATE TABLE department(
    department_id INTEGER primary key,
    department_name TEXT
);

CREATE TABLE people(
    people_id INTEGER primary key,
    name TEXT,
    original_name TEXT,
    gender INTEGER,
    popularity NUMERIC,
    department_id INTEGER REFERENCES department(department_id)
);
