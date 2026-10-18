# Contributing & Gitflow Workflow

This project follows **Gitflow**. Nobody commits directly to `main` or `develop`;
all work goes through feature branches and Pull Requests (PRs).

## Branches

| Branch | Purpose | Who merges into it |
|---|---|---|
| `main` | Stable, demo-ready code. Jenkins deploys from here. | Merged from `develop` via PR |
| `develop` | Integration branch where finished features come together | Merged from `feature/*` via PR |
| `feature/application` | Flask app + tests (Member 1) | |
| `feature/git-workflow` | Gitflow, PR template, webhook docs (Member 2) | |
| `feature/docker` | Dockerfile + docker-compose (Member 3) | |
| `feature/jenkins` | Jenkinsfile + pipeline (Member 4) | |
| `feature/kubernetes` | `k8s/` manifests + scaling (Member 5) | |

```
main      ●───────────────────────●────────●
           \                     /        /
develop     ●──●─────●──────●───●────●───●
               \    /        \  /
feature/docker  ●──●          ●  (merged back via PR)
```

## Day-to-day workflow

```bash
# 1. Start from an up-to-date develop
git checkout develop
git pull origin develop

# 2. Create your feature branch
git checkout -b feature/<name>

# 3. Work, then commit often
git add .
git commit -m "feat: short description"

# 4. Push the branch and open a Pull Request into develop
git push -u origin feature/<name>
```

Then on GitHub: **Pull requests → New pull request**, base `develop`,
compare `feature/<name>`. At least one teammate reviews before merging.

## Release to main
When `develop` is stable and tests pass:
open a PR **`develop` → `main`**. Merging into `main` is what triggers
the Jenkins deployment pipeline.

## Commit message convention

| Prefix | Use for |
|---|---|
| `feat:` | new feature |
| `fix:` | bug fix |
| `docs:` | documentation only |
| `test:` | tests |
| `ci:` | Jenkinsfile / pipeline |
| `chore:` | Docker, k8s, config, tooling |

Example: `ci: add docker build stage to Jenkinsfile`

## Rules
1. Never push directly to `main` or `develop`.
2. Every PR needs at least 1 review.
3. Tests (`pytest -v`) must pass before opening a PR.
4. Keep PRs small and focused.
5. Delete the feature branch after it is merged.
