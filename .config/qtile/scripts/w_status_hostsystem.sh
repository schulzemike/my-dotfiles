#!/bin/bash
text=" "

if [[ "$(ls -1 ~/shared-drives | wc -l)" > 0 ]]; then
    printf "<span>${text}</span>"
else
    printf "<span foreground='$1'>${text}</span>"
fi
