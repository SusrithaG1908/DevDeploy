"""
Student Management System
Member 1 deliverable: Application + Testing
A real (small) web app with HTML pages, not just raw text responses.
"""

from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

students = [
    {"id": 1, "name": "Susritha", "branch": "CSE", "year": 4},
    {"id": 2, "name": "Rahul", "branch": "ECE", "year": 3},
    {"id": 3, "name": "Priya", "branch": "IT", "year": 2},
]
next_id = 4


@app.route("/")
def home():
    return render_template("index.html", students=students, count=len(students))


@app.route("/add", methods=["POST"])
def add_student():
    global next_id
    name = request.form.get("name", "").strip()
    branch = request.form.get("branch", "").strip()
    year = request.form.get("year", "").strip()

    if name and branch and year:
        students.append({"id": next_id, "name": name, "branch": branch, "year": int(year)})
        next_id += 1

    return redirect(url_for("home"))


@app.route("/delete/<int:student_id>", methods=["POST"])
def delete_student(student_id):
    global students
    students = [s for s in students if s["id"] != student_id]
    return redirect(url_for("home"))


@app.route("/health")
def health():
    return jsonify({"status": "healthy"})


@app.route("/api/students")
def api_students():
    return jsonify({"students": students})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
