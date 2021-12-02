#!/usr/bin/env bash

set -eu

repo_uri="https://x-access-token:${DEPLOY_TOKEN}@github.com/${GITHUB_REPOSITORY}.git"
remote_name="origin"

cd "$GITHUB_WORKSPACE"

git config user.name "$GITHUB_ACTOR"
git config user.email "${GITHUB_ACTOR}@bots.github.com"

git add .
git commit -m "add new plugin"
if [ $? -ne 0 ]; then
    echo "nothing to commit"
    exit 0
fi

git push --force-with-lease "$remote_name" "$GITHUB_REF_NAME"