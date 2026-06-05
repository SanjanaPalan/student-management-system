from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create Database
def init_db():
    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS students(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        department TEXT,
        semester TEXT,
        email TEXT,
        attendance INTEGER
    )
    """)

    conn.commit()
    conn.close()

init_db()


@app.route('/')
def home():

    department = request.args.get('department')
    semester = request.args.get('semester')

    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    query = "SELECT * FROM students WHERE 1=1"
    params = []

    if department:
        query += " AND department=?"
        params.append(department)

    if semester:
        query += " AND semester=?"
        params.append(semester)

    cur.execute(query, params)
    students = cur.fetchall()

    cur.execute("SELECT COUNT(*) FROM students")
    total_students = cur.fetchone()[0]

    cur.execute("SELECT AVG(attendance) FROM students")
    avg_attendance = cur.fetchone()[0]

    if avg_attendance is None:
        avg_attendance = 0

    conn.close()

    return render_template(
        "index.html",
        students=students,
        total_students=total_students,
        avg_attendance=round(avg_attendance, 1)
    )


@app.route('/add')
def add_page():
    return render_template("add_student.html")


@app.route('/add_student', methods=['POST'])
def add_student():

    name = request.form['name']
    department = request.form['department']
    semester = request.form['semester']
    email = request.form['email']
    attendance = request.form['attendance']

    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    cur.execute("""
    INSERT INTO students
    (name, department, semester, email, attendance)
    VALUES (?, ?, ?, ?, ?)
    """,
    (name, department, semester, email, attendance))

    conn.commit()
    conn.close()

    return redirect('/')


@app.route('/delete/<int:id>')
def delete_student(id):

    conn = sqlite3.connect("students.db")
    cur = conn.cursor()

    cur.execute(
        "DELETE FROM students WHERE id=?",
        (id,)
    )

    conn.commit()
    conn.close()

    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)