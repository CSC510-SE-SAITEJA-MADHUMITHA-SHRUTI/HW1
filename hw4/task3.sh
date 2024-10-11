#!/bin/bash

gawk -F, '$3 == 2 && $13 ~ /S/ {print $0}' /Users/shrutichintalapati/Downloads/hw4/titanic.csv | \
sed 's/female/F/g; s/male/M/g' | \
tee /dev/tty | \
gawk -F, '{
    if ($7 != "") { 
        sum += $7; 
        count++; 
    } 
} 
END {
    if (count > 0) 
        print "Average Age:", sum / count; 
    else 
        print "No age present.";
}'
