#!/usr/bin/env bash
# Creates the Gitflow branch structure for DevDeploy and pushes it to GitHub.
# Run once, from the repository root, after authenticating with GitHub.
set -e

git checkout main
git pull origin main

# develop branch
git checkout -B develop
git push -u origin develop

# feature branches (one per team area), all branched from develop
for b in feature/application feature/git-workflow feature/docker feature/jenkins feature/kubernetes; do
  git checkout develop
  git checkout -B "$b"
  git push -u origin "$b"
done

git checkout develop
echo "Gitflow branches created: main, develop, feature/*"
