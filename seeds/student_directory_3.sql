DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS cohorts;
-- Create the table without the foreign key first.
CREATE TABLE cohorts (
  id SERIAL PRIMARY KEY,
  name text,
  start_date date
);

-- Then the table with the foreign key second.
CREATE TABLE students (
  id SERIAL PRIMARY KEY,
  name text,
  cohort_name text,
  cohort_id int,
  constraint fk_cohort foreign key(cohort_id)
    references cohorts(id)
    on delete cascade
);