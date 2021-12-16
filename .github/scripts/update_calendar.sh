#!/bin/bash

day=$(date +%d)
title=$(curl -s "https://adventofcode.com/2021/day/$day" | grep -o "<h2>.*</h2>" | sed -E "s/<h2>--- Day.*: (.*) ---<\/h2>/\1/g")
echo ".. | $day: $title ([puzzle text](https://adventofcode.com/2021/day/$day)) | | |" | tee -a README.md
