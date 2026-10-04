# Student Management System — Application + Testing

## What this is
A small but real Flask web app — an actual page with a form and a live
student roster (not just plain text). This is the application that the
rest of the team containerizes, pipelines through Jenkins, and deploys
to Kubernetes.

## Pages / routes
| Route | Method | What it does |
|---|---|---|
| `/` | GET | The student management page — add/remove students, see the roster |
| `/add` | POST | Adds a student from the form |
| `/delete/<id>` | POST | Removes a student |
| `/health` | GET | Health check → `{"status": "healthy"}` (used by Kubernetes/monitoring) |
| `/api/students` | GET | JSON list of students, for anyone who wants raw data |

## Project structure
```
student-app/
├── app.py
├── templates/
│   └── index.html
├── test_app.py
├── requirements.txt
└── README.md
```

## Run locally
```bash
pip install -r requirements.txt
python app.py
# open http://localhost:5000 in a browser
```

## Run tests
```bash
pytest -v
```
