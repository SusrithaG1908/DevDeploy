# Student Management System — Application + Testing (Member 1)

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
Expected: `6 passed`

## Handoff notes for the team
- **Member 3 (Docker):** app listens on `0.0.0.0:5000`. The `templates/`
  folder must be copied into the image alongside `app.py` — don't just
  copy `app.py` on its own, or Flask won't find the HTML page.
- **Member 4 (Jenkins):** test stage should run
  `pip install -r requirements.txt && pytest`. If that fails, the
  pipeline should stop before the Docker build stage.
- **Member 5 (Kubernetes):** container port is `5000` — `containerPort: 5000`
  in `deployment.yaml`, `targetPort: 5000` in `service.yaml`. `/health`
  is a good liveness/readiness probe path.
- **Demo tip:** for the "developer pushes a code change" step, edit the
  `<p>` line in `templates/index.html` (e.g. the subtitle text) or add a
  student live on screen — either one is a visible change that flows
  through the whole pipeline and shows up in the browser after deploy.
