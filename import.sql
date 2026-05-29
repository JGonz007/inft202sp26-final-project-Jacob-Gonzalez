-- Import Worksheet
-- Run this in Adminer while connected to the Docker database `final`.
--
-- This file loads popular_people.csv into a temporary staging table first.
-- Then it fills the related department and people tables.

DROP TABLE IF EXISTS popular_people_staging;

CREATE TEMP TABLE popular_people_staging (
    name TEXT,
    gender INTEGER,
    known_for_department TEXT,
    original_name TEXT,
    popularity NUMERIC
);

COPY popular_people_staging (name, gender, known_for_department, original_name, popularity)
FROM '/project/popular_people.csv'
DELIMITER ','
CSV HEADER;

INSERT INTO department (department_id, department_name)
SELECT
    ROW_NUMBER() OVER (ORDER BY cleaned_department) AS department_id,
    cleaned_department AS department_name
FROM (
    SELECT DISTINCT
        COALESCE(NULLIF(TRIM(known_for_department), ''), 'Unknown') AS cleaned_department
    FROM popular_people_staging
) AS unique_departments;

INSERT INTO people (people_id, name, original_name, gender, popularity, department_id)
SELECT
    ROW_NUMBER() OVER (ORDER BY s.name, s.original_name, s.popularity) AS people_id,
    s.name,
    s.original_name,
    s.gender,
    s.popularity,
    d.department_id
FROM popular_people_staging AS s
JOIN department AS d
    ON d.department_name = COALESCE(NULLIF(TRIM(s.known_for_department), ''), 'Unknown');

-- After running the import, run these checks:
SELECT COUNT(*) FROM department;
SELECT COUNT(*) FROM people;
