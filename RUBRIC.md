# INFT202 Final Project Rubric

## Overview

Students choose a multi-table dataset, explore it, design a relational schema, import it into PostgreSQL, write 8 SQL queries, and submit a working Flask web dashboard. The AI assistant guides them through each step in small chunks, but the table-creation SQL and query SQL are the student's own work.

**Total: 100 points**

---

## 1. Data Exploration & Schema Design (25 pts)

| Criteria | Points |
|----------|--------|
| Dataset has at least 2 related tables that can be linked together | 5 |
| `data_exploration.md` shows thoughtful exploration of rows, columns, possible keys, categories, measurements, and data quality | 5 |
| `schema_plan.md` explains the table design, column choices, data types, primary keys, and foreign key relationship | 5 |
| `table_creation.sql` is student-written and uses appropriate PostgreSQL types, primary keys, and at least one foreign key constraint | 5 |
| Data successfully imported - tables have expected row counts | 5 |

---

## 2. Guided SQL Queries (35 pts - 6 queries)

Each query is saved as `queries/query_N.sql`. The assistant gives the prompt and hints, but the student writes and runs the SQL in Adminer or Beekeeper Studio before the final query is saved.

| Query | Concept | Points |
|-------|---------|--------|
| Query 1 | `SELECT` + `WHERE` + `ORDER BY` + `LIMIT` - filter and sort | 5 |
| Query 2 | `COUNT(*)` + `GROUP BY` - count by category | 6 |
| Query 3 | `AVG`/`SUM`/`MIN`/`MAX` + `GROUP BY` - aggregate by category | 6 |
| Query 4 | `GROUP BY` + `HAVING` - filter aggregated groups | 6 |
| Query 5 | `JOIN` - combine both tables | 6 |
| Query 6 | `JOIN` + `GROUP BY` + aggregate - the full combo | 6 |

Grading each query: Full credit if the query runs, returns meaningful results, and uses the specified concept. Half credit if syntactically correct but doesn't answer the intended question. Zero if it doesn't run.

---

## 3. Discussion Queries (20 pts - 2 queries x 10 pts each)

Saved in `discussion/discussion_1.sql` and `discussion/discussion_2.sql`.

| Criteria | Points |
|----------|--------|
| Query runs and returns useful results | 5 |
| Student's written explanation (2-3 sentences) reflects what the data actually shows | 5 |

---

## 4. Web Dashboard (20 pts)

| Criteria | Points |
|----------|--------|
| App runs with Docker and connects to PostgreSQL | 5 |
| Dashboard page shows at least 2 summary stats and 1 Chart.js chart | 5 |
| Browse page shows paginated data | 5 |
| Insights page shows discussion query results with student's explanations | 5 |

---

## 5. Submission (bonus: up to 5 pts)

| Criteria | Points |
|----------|--------|
| GitHub repo with complete commit history | 3 |
| `README.md` describes the dataset, tables, and queries | 2 |

---

## What The Assistant Handles vs. What The Student Handles

| Assistant handles | Student handles |
|---------------|-----------------|
| Data exploration prompts and summaries | Discussing what the data means and what looks important |
| Schema design guidance | Choosing primary keys, foreign keys, and table relationships |
| `schema_plan.md` and a `table_creation.sql` worksheet | Writing and running the actual `CREATE TABLE` commands |
| Import commands | Running the import, troubleshooting row count issues |
| Hints and explanations | Writing and running every graded SQL query in Adminer or Beekeeper Studio |
| Entire Flask web app | Configuring `.env`, running the server, testing it |
| README template | Filling in their dataset description and query explanations |

The table-creation file, SQL files in `queries/`, and SQL files in `discussion/` are primary academic deliverables. The assistant guides but does not write them.
