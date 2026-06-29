#!/usr/bin/env bash

declare -A files=(
    ["qtile"]="$XDG_DATA_HOME/qtile/qtile.log"
)

choice=$(printf '%s\n' "${!files[@]}" | sort | rofi -dmenu -p "Action: [Enter] Edit | [Alt+1] Clear" -theme-str 'element-icon { enabled: false; }')

status=$?

[[ -z "$choice" ]] && exit 0

case $status in
    0) exec kitty nvim "${files[$choice]}" ;;
    10) 
        > "${files[$choice]}" 
        notify-send "Cleared ${files[$choice]}" ;;
esac
