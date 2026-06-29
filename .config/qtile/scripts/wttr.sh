#!/usr/bin/env bash

OUTPUT_FILE=/tmp/wttr.png
DIAGRAM_FILE=/tmp/wttr2.png
[[ -v LOCATION ]] && loc=$LOCATION || loc=Berlin


curl --output $OUTPUT_FILE wttr.in/$loc.png?QF\&lang=de\&background=3c3836 > /dev/null 2>&1
curl --output $DIAGRAM_FILE v2.wttr.in/$loc.png?QF\&lang=de\&background=3c3836 > /dev/null 2>&1
curl -s wttr.in/$loc?format=1 || echo "N/A"
