#!/bin/sh

# Variables can either be defined and directly used...
SOME_VAR="Hello World!"
echo "${SOME_VAR}"

# I have to run this in bash terminal first to initialize REPO_URL variable
# REPO_URL="some-url" ./q2.sh
git clone "${REPO_URL}" repo
cd repo
printf "ccc" > c.txt
git add c.txt
git commit -m "Add new file c.txt with some content"
git push origin main  