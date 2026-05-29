# Schema Plan: Popular People

## Design Goal

We are keeping the design simple so the database is easy to build and query. The main analysis focus is popularity scores, especially comparing popularity across departments.

## Tables

### `departments`

This table stores the repeated department names from the CSV.

| Column | Suggested Type | Notes |
|---|---|---|
| `department_id` | `INTEGER` | Primary key. A generated number for each department. |
| `department_name` | `TEXT` | The department name, such as Acting, Directing, or Writing. |

Why this table exists: department names repeat thousands of times in the CSV, so separating them gives us a clean related table.

### `people`

This table stores one row per person record from the CSV.

| Column | Suggested Type | Notes |
|---|---|---|
| `person_id` | `INTEGER` | Primary key. A generated number for each person record. |
| `name` | `TEXT` | The person's display name. |
| `original_name` | `TEXT` | The person's original name. |
| `gender` | `INTEGER` | The numeric gender code from the dataset. |
| `popularity` | `NUMERIC` | The popularity score. This is the main measurement we want to analyze. |
| `department_id` | `INTEGER` | Foreign key that connects each person to a row in `departments`. |

Why this table exists: it contains the main person information and keeps the popularity score attached to the person it describes.

## Relationship

The relationship is:

> Many people can belong to one department.

That means:

- `departments.department_id` identifies one department.
- `people.department_id` points to the department for each person.

## Columns From The CSV

Original CSV columns:

- `name`
- `gender`
- `known_for_department`
- `original_name`
- `popularity`

Planned changes:

- `known_for_department` will become rows in the `departments` table.
- `people` will store `department_id` instead of repeating the full department name.
- Because names repeat, `name` should not be used as the primary key.
- A generated `person_id` is safer for the `people` table.

## Analysis Questions This Schema Supports

1. Which people have the highest popularity scores?
2. Which departments have the highest average popularity?
3. How many people are listed in each department?
4. Which department has the most highly popular people?
5. How does popularity vary between Acting, Directing, Writing, and other departments?
