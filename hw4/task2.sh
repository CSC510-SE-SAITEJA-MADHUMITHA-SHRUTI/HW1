#!/bin/bash

# Find files containing "sample" and count occurrences of "CSC510"
grep -rl "sample" dataset1 | \
xargs -I{} bash -c 'count=$(grep -o "CSC510" "{}" | wc -l); if [ "$count" -ge 3 ]; then filesize=$(wc -c < "{}"); echo "$count $filesize {}"; fi' | \
gawk '{ printf "%s %s %s\n", $1, $2, gensub(/file_/, "filtered_", "g", $3) }' | \
sort -k1,1nr -k2,2nr
