# Data Exploration: Popular People

## Source File

### `popular_people.csv`

This file contains 9,980 rows of people connected to film/television/media work. One row appears to represent one person record, with a name, gender code, main department, original name, and a popularity score.

First few rows:

| name | gender | known_for_department | original_name | popularity |
|---|---:|---|---|---:|
| Eric Larson | 2 | Visual Effects | Eric Larson | 47.978 |
| Robert Middlemass | 2 | Acting | Robert Middlemass | 47.8017 |
| María Vaner | 1 | Acting | María Vaner | 47.2016 |
| Carl Wharton | 2 | Acting | Carl Wharton | 36.3365 |
| Victor Moore | 2 | Acting | Victor Moore | 35.9181 |

## Important Columns

| Column | What It Seems To Mean | Possible Type |
|---|---|---|
| `name` | The person's display name | `TEXT` |
| `gender` | A numeric gender code. Values include 0, 1, 2, and 3. | `INTEGER` |
| `known_for_department` | The main department or job area the person is known for, such as Acting, Directing, or Writing. | `TEXT` |
| `original_name` | The person's original or non-localized name. Often the same as `name`. | `TEXT` |
| `popularity` | A numeric popularity score. Higher values appear to mean the person is more popular in the source dataset. | `NUMERIC` |

## Data Quality Notes

- The file has 9,980 data rows.
- There are no blank values in `name`, `gender`, `original_name`, or `popularity`.
- There are 5 blank values in `known_for_department`.
- `popularity` ranges from 0.5784 to 47.978, with an average around 2.124.
- The most common department is `Acting`, with 9,320 rows.
- Other departments include `Directing`, `Writing`, `Production`, `Sound`, `Editing`, `Visual Effects`, `Crew`, `Art`, `Costume & Make-Up`, `Camera`, `Lighting`, and `Creator`.
- Some names repeat. There are 2,142 names that appear more than once, so `name` alone is probably not a safe primary key.
- The dataset does not include an obvious ID column, so we may need to create our own person ID when designing tables.

## Possible Primary Keys and Foreign Keys

Because the CSV has one file instead of multiple source files, we can still design related tables by separating repeated category information into lookup tables.

Possible tables:

- A main `people` table for one row per person record.
- A `departments` lookup table for department names.
- A `gender_codes` lookup table for the gender code values.

Possible keys:

- `people` could use a generated ID as its primary key because `name` repeats.
- `departments` could use a generated department ID or the department name as its identifier.
- `gender_codes` could use the numeric gender code as its identifier.
- `people` could connect to `departments` through a department ID or department name.
- `people` could connect to `gender_codes` through the gender code.

## Interesting Analysis Questions

1. Which departments have the most people in this dataset?
2. Which departments have the highest average popularity?
3. Which gender code appears most often in the dataset?
4. Who are the most popular people in a specific department, such as Acting or Directing?
5. Are some departments represented by only a small number of people?

## Questions To Think About

- What do you think one row represents: a unique person, or a person appearance from the source system?
- Which category feels more interesting to analyze: department or gender?
- Since names repeat, what would you choose as the safest way to identify one row?
- Do the gender codes make sense to you, or should we treat them as codes and keep their meaning cautious?
