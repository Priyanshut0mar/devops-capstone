
import os
import sqlite3
import logging
from flask import Flask, request, redirect, url_for, render_template

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE = os.path.join(BASE_DIR, "students.db")

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def get_db():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE,
            course TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
def home():
    conn = get_db()
    students = conn.execute(
        "SELECT * FROM students ORDER BY id DESC"
    ).fetchall()
    conn.close()
    return render_template("index.html", students=students)


@app.route("/add", methods=["POST"])
def add_student():
    name = request.form.get("name", "").strip()
    email = request.form.get("email", "").strip()
    course = request.form.get("course", "").strip()

    if not name or not email or not course:
        return "All fields are required", 400

    try:
        conn = get_db()
        conn.execute(
            "INSERT INTO students (name, email, course) VALUES (?, ?, ?)",
            (name, email, course)
        )
        conn.commit()
        conn.close()
        logger.info("Student added: %s", email)

    except sqlite3.IntegrityError:
        return "Email already exists", 409

    return redirect(url_for("home"))


@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    conn = get_db()
    conn.execute("DELETE FROM students WHERE id = ?", (student_id,))
    conn.commit()
    conn.close()

    logger.info("Student deleted: ID %s", student_id)
    return redirect(url_for("home"))


@app.route("/health")
def health():
    try:
        conn = get_db()
        conn.execute("SELECT 1")
        conn.close()
        return {"status": "healthy", "database": "connected"}, 200
    except sqlite3.Error:
        return {"status": "unhealthy", "database": "disconnected"}, 503


init_db()

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000))
    )
