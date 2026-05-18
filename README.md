# INFT202 - Database Final Project

This project uses Codex and Docker to guide you through a database final project in small steps: choosing data, exploring it, designing linked tables, writing SQL, and building a small Flask dashboard.

## Start Here

1. Fork this repo on GitHub.
2. Clone your fork:

```bash
git clone https://github.com/YOUR_USERNAME/inft202-final-project.git
cd inft202-final-project
```

3. Open Codex and choose this project folder as the workspace.
4. In Codex, run the local agent skill by saying:

```text
Load the db-final-project skill and start the final project guide.
```

Codex will detect which phase you are in and tell you the next step.

Codex's first job is to run `scripts/setup_check.py`. That script checks your GitHub setup, starts the Docker database bundle, and verifies a PostgreSQL database named `final`.

## What You Need Installed

- Git
- Docker Desktop
- Codex
- A GitHub account

You do not need to install PostgreSQL, Python, pip, or Flask directly on your computer. Docker runs the database and app environment for this project.

## What You Will Create

- `data_exploration.md` - notes from exploring your dataset
- `schema_plan.md` - your table design and table relationships
- `table_creation.sql` - your own `CREATE TABLE` commands
- `import.sql` - helper commands for loading data
- `queries/query_1.sql` through `queries/query_6.sql` - guided SQL queries
- `discussion/discussion_1.sql` and `discussion/discussion_2.sql` - your own analysis queries
- A Flask dashboard generated after your SQL work is complete

## Database Workflow

The Docker setup starts:

- PostgreSQL at `localhost:5432`
- Adminer, a browser database tool, at `http://localhost:8080`

To use **Adminer**, open `http://localhost:8080` and enter:

- System/server: `PostgreSQL`
- Server: `postgres`
- Username: `postgres`
- Password: `postgres`
- Database: `final`

To use **Beekeeper Studio**, create a new Postgres connection and enter:

- Host: `localhost`
- Port: `5432`
- User: `postgres`
- Password: `postgres`
- Default database: `final`

Write and run SQL in Adminer or Beekeeper Studio, then paste your query and a few result rows back into Codex. Codex will help you debug and will save your finished query files.

Codex can guide you, but it should not write your final `CREATE TABLE` commands or graded query SQL for you.

## Submit

When finished, push your work to GitHub and submit the repo link on Canvas:

```bash
git add .
git commit -m "Final project complete"
git push
```

Your `.env` file should stay out of GitHub because it may contain your database password.

See [RUBRIC.md](RUBRIC.md) for grading details.
