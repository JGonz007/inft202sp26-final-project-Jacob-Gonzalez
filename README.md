# Popular People Database Project

This INFT202 final project uses a popular people dataset to explore popularity scores across media departments. The project includes a PostgreSQL database, related tables, SQL analysis queries, and a Flask web dashboard.

## Dataset

The dataset file is `popular_people.csv`. It contains 9,980 people records with these columns:

- `name`
- `gender`
- `known_for_department`
- `original_name`
- `popularity`

One row represents one person record. The main analysis focus is the `popularity` score and how popularity differs across departments such as Acting, Directing, Writing, Visual Effects, and Production.

## Data Exploration

During exploration, I found that `Acting` is by far the largest department in the dataset. I also found that some department names repeat many times, names are not unique, and a few rows have a blank department value. Because names repeat, I used a generated ID instead of using `name` as the primary key.

## Database Schema

The database uses two related tables:

### `department`

Stores one row for each department.

- `department_id` - primary key
- `department_name` - readable department name

### `people`

Stores one row for each person record.

- `people_id` - primary key
- `name`
- `original_name`
- `gender`
- `popularity`
- `department_id` - foreign key connected to `department.department_id`

The relationship is one department to many people.

## Guided SQL Queries

The six guided SQL queries are saved in the `queries/` folder.

1. `query_1.sql` - Finds the 10 most popular people in the Acting department.
2. `query_2.sql` - Counts how many people are listed in each department.
3. `query_3.sql` - Calculates the average popularity score for each department.
4. `query_4.sql` - Filters departments to those with average popularity above 2 and at least 10 people.
5. `query_5.sql` - Joins people with department names and shows the 20 most popular people overall.
6. `query_6.sql` - Joins both tables, groups by department name, and calculates average popularity and total people.

## Discussion Queries

The discussion queries are saved in the `discussion/` folder.

### Small Departments With High Average Popularity

This query finds departments with fewer than 50 people and ranks them by average popularity.

Student explanation:

> What really surprises me is that there is an unknown category in the department name, whether this is an error or not this is a bit confusing to me. What also amazes me is that there is very little popularity for the production department even with 43 people working in it.

### High-Popularity People by Department

This query counts people in each department with a popularity score above 10.

Student explanation:

> This tells me that Acting has a high poupularity count, with a total of 67. Meanwhile Visual effects is shockingly low with only 1 popularity count.

## Web Dashboard

The Flask dashboard includes:

- Dashboard page with summary statistics and charts
- Browse page with pagination and name search
- Insights page showing the two discussion queries and explanations

The app connects to the PostgreSQL database running in Docker.

## How To Run

Start the database and Adminer:

```bash
python scripts/setup_check.py
```

If `python` does not work on Windows, use the bundled Codex setup or run the setup check from Codex.

Open Adminer:

```text
http://localhost:8080
```

Adminer login:

- System: `PostgreSQL`
- Server: `postgres`
- Username: `postgres`
- Password: `postgres`
- Database: `final`

Start the Flask dashboard:

```bash
docker compose --profile app up --build
```

Open the dashboard:

```text
http://localhost:5000
```

## Files

- `data_exploration.md` - data exploration notes
- `schema_plan.md` - relational schema plan
- `table_creation.sql` - table creation SQL
- `import.sql` - CSV import and table population SQL
- `queries/` - six guided SQL challenges
- `discussion/` - two student-selected discussion queries and explanations
- `app.py` - Flask app
- `templates/` - dashboard HTML templates

## Security Note

The `.env` file stores local database connection settings and is ignored by Git.
