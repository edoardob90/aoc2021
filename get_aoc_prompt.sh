#!/bin/bash
# must supply the day index
[[ "$#" < 1 ]] && echo -e "Day number is missing!\nUSAGE: $(basename $0) <day number> [<year>]" >&2 && exit 1

# system must have Pandoc
if ! type pandoc 2>&1 >/dev/null; then
    echo "The script requires Pandoc! Install it and re-run the script" >&2
    exit 1
fi

# full path of the script's directory
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

# just make sure the destination directory exists
DEST="$DIR/$1"
mkdir -p "$DEST"

# get html with pandoc and convert it to md
$(which pandoc) -f html -t gfm --wrap=preserve "https://adventofcode.com/${2:-2021}/day/$1" | \
awk '{
    if ($0 ~ /<div role="main">/) {
        getline
        while ($0 !~ /^To play/) {
            if ($0 ~ /^#+/) {
                title=substr($0, index($0, "Day"))
                sub(/---/, "", title)
                printf("# %s\n", title)
            } else print $0
            getline
        }
    }
}' > ${DEST}/README.md

# get the input (if a .cookie file is present)
if [[ -f "$DIR/.cookie" ]]; then
    if ! type $(which curl) 2>&1 >/dev/null; then
        echo "curl not found!" >&2
        exit 1
    fi
    curl -s "https://adventofcode.com/${2:-2021}/day/$1/input" --cookie "session=$(cat ${DIR}/.cookie)" > ${DEST}/input.txt
fi
