#!/bin/bash
text=" "

if [[ "$(ls -1 /hostsystem | wc -l)" > 0 ]]; then
    printf "<span>${text}</span>"
else
    printf "<span foreground='$1'>${text}</span>"
fi
