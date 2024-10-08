#!/bin/bash

grep -rl "sample" dataset1/ | xargs -I{} sh -c '
    count=$(grep -o "CSC510" "{}" | wc -l)
    if [ "$count" -ge 3 ]; then
        echo "$count {}"
    fi
' | sort -k1,1nr -k2,2 | perl -pe 's/file_/filtered_/g; s/^\d+\s+//g' > output.txt

# output

cat output.txt
