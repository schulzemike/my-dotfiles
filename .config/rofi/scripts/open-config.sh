#!/usr/bin/env bash

declare -A files=(
    ["qtile"]="$XDG_CONFIG_HOME/qtile/myconfig.py"
    ["quickmarks"]="$XDG_CONFIG_HOME/qutebrowser/quickmarks"
)

choice=$(printf '%s\n' "${!files[@]}" | sort | rofi -dmenu -p "open config" -show-icons false -theme-str 'element-icon { enabled: false; }')

[[ -z "$choice" ]] && exit 0

exec kitty nvim "${files[$choice]}"
