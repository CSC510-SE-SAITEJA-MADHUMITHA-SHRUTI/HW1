#!/bin/bash

grep -rl "sample" dataset1/ | xargs -n 1 grep -o "CSC510" | sort | uniq -c | awk '$1 >= 3 {print $2}' | sed 's/file_/filtered_/g' > output.txt

# Output
cat output.txt
