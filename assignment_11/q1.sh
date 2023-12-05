#!/bin/sh

# Add your terminal commands here. Make sure to first run them
# locally on your machine to have more detailed error output.
echo "Hello World!"
git init
printf "aaa" > a.txt
printf "bbb" > b.txt
git add a.txt b.txt
git commit -m "Added both a and b files"
printf "\nb2" >> b.txt
git add b.txt
git commit -m "Added second line to b.txt"