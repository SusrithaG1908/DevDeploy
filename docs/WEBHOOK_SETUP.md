# GitHub → Jenkins Webhook Setup

Goal: every `git push` to this repository automatically starts a Jenkins build.

```
git push → GitHub → Webhook → Jenkins → Test → Docker Build → Deploy
```

> Member 2 (Git/GitHub) and Member 4 (Jenkins) set this up together.

## 1. Make Jenkins reachable from GitHub
GitHub must be able to reach Jenkins over the internet. If Jenkins runs on a
laptop (`localhost:8080`), expose it with a tunnel such as **ngrok**:

```bash
ngrok http 8080
# gives a URL like https://abcd-1234.ngrok-free.app
```

## 2. Jenkins side (Member 4)
1. Install the **GitHub Integration** / **Git** plugins.
2. Create a **Pipeline** job and choose *Pipeline script from SCM*.
   - SCM: Git
   - Repository URL: `https://github.com/SusrithaG1908/DevDeploy.git`
   - Branch: `*/main`
   - Script Path: `Jenkinsfile`
3. In *Build Triggers*, tick **GitHub hook trigger for GITScm polling**.

## 3. GitHub side (Member 2)
1. Open the repo → **Settings → Webhooks → Add webhook**.
2. Fill in:
   - **Payload URL:** `http://<jenkins-public-url>/github-webhook/`  (trailing slash required)
   - **Content type:** `application/json`
   - **Events:** *Just the push event*
   - **Active:** ticked
3. Click **Add webhook**.

## 4. Verify
- GitHub → Settings → Webhooks → *Recent Deliveries* should show a green tick (HTTP 200).
- Push a small change; a new build should appear in Jenkins within seconds.

## Troubleshooting
| Symptom | Fix |
|---|---|
| Red cross / timeout in Recent Deliveries | Jenkins URL not publicly reachable; check ngrok is running |
| 403 from Jenkins | Enable the GitHub hook trigger, or check CSRF/crumb settings |
| Build doesn't start | Job must have *GitHub hook trigger for GITScm polling* ticked |
| ngrok URL changed | Update the Payload URL in GitHub (free ngrok URLs change on restart) |
