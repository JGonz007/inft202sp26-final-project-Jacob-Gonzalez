import math
import os

import psycopg2
from dotenv import load_dotenv
from flask import Flask, render_template, request
from psycopg2.extras import RealDictCursor

load_dotenv()

app = Flask(__name__)


def get_connection():
    return psycopg2.connect(
        dbname=os.getenv("DB_NAME", "final"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "postgres"),
        host=os.getenv("DB_HOST", "postgres"),
        port=os.getenv("DB_PORT", "5432"),
    )


def fetch_all(sql, params=None):
    with get_connection() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute(sql, params or ())
            return cursor.fetchall()


def fetch_one(sql, params=None):
    rows = fetch_all(sql, params)
    return rows[0] if rows else {}


def load_sql_file(path):
    with open(path, "r", encoding="utf-8") as file:
        return file.read()


@app.route("/")
def index():
    stats = {
        "total_people": fetch_one("SELECT COUNT(*) AS value FROM people")["value"],
        "total_departments": fetch_one("SELECT COUNT(*) AS value FROM department")["value"],
        "avg_popularity": round(fetch_one("SELECT AVG(popularity) AS value FROM people")["value"], 2),
        "high_popularity": fetch_one("SELECT COUNT(*) AS value FROM people WHERE popularity > 10")["value"],
    }

    count_by_department = fetch_all(
        """
        SELECT department.department_name, COUNT(people.people_id) AS total_people
        FROM department
        JOIN people ON department.department_id = people.department_id
        GROUP BY department.department_id, department.department_name
        ORDER BY total_people DESC
        LIMIT 10;
        """
    )
    avg_by_department = fetch_all(
        """
        SELECT department.department_name, AVG(people.popularity) AS average_popularity
        FROM department
        JOIN people ON department.department_id = people.department_id
        GROUP BY department.department_id, department.department_name
        ORDER BY average_popularity DESC
        LIMIT 10;
        """
    )

    return render_template(
        "index.html",
        stats=stats,
        count_by_department=count_by_department,
        avg_by_department=avg_by_department,
    )


@app.route("/browse")
def browse():
    page = max(request.args.get("page", 1, type=int), 1)
    search = request.args.get("q", "").strip()
    per_page = 25
    offset = (page - 1) * per_page

    where = ""
    params = []
    if search:
        where = "WHERE people.name ILIKE %s OR people.original_name ILIKE %s"
        search_term = f"%{search}%"
        params.extend([search_term, search_term])

    total = fetch_one(
        f"""
        SELECT COUNT(*) AS value
        FROM people
        JOIN department ON department.department_id = people.department_id
        {where};
        """,
        params,
    )["value"]

    rows = fetch_all(
        f"""
        SELECT people.people_id, people.name, people.original_name, people.gender,
               people.popularity, department.department_name
        FROM people
        JOIN department ON department.department_id = people.department_id
        {where}
        ORDER BY people.popularity DESC, people.name
        LIMIT %s OFFSET %s;
        """,
        params + [per_page, offset],
    )

    pages = max(math.ceil(total / per_page), 1)
    return render_template(
        "browse.html",
        rows=rows,
        page=page,
        pages=pages,
        search=search,
        total=total,
    )


@app.route("/insights")
def insights():
    insight_1 = fetch_all(load_sql_file("discussion/discussion_1.sql"))
    insight_2 = fetch_all(load_sql_file("discussion/discussion_2.sql"))
    explanation_1 = load_sql_file("discussion/discussion_1_explanation.txt")
    explanation_2 = load_sql_file("discussion/discussion_2_explanation.txt")

    return render_template(
        "insights.html",
        insights=[
            {
                "question": "Which departments have a small number of people but surprisingly high average popularity?",
                "explanation": explanation_1,
                "rows": insight_1,
            },
            {
                "question": "How many people in each department have a popularity score above 10?",
                "explanation": explanation_2,
                "rows": insight_2,
            },
        ],
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
