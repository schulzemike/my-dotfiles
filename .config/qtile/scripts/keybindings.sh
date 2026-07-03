#!/usr/bin/env bash

CONFIG_PATH="$HOME/.config/qtile"
QTILE_CONFIG="${CONFIG_PATH}/myconfig.py"

if [ ! -f "$QTILE_CONFIG" ]; then
    echo "Error: Qtile config not found at ${QTILE_CONFIG}"
    exit 1
fi

KEY_LIST=$(python3 ${CONFIG_PATH}/scripts/extractKeybindings.py ${QTILE_CONFIG})

FORMATTED_LIST=$(echo "$KEY_LIST" | while IFS=$'\t' read -r col1 col2; do
    # Skip empty lines
    [ -z "$col1" ] && continue
    # %-40s forces col1 to take exactly 40 characters of width, left-aligned
    printf "%-40s%s\n" "$col1" "$col2"
done)


# Launch Rofi with tab-alignment configuration
# This pushes the description cleanly to the 50% mark
echo -e "$FORMATTED_LIST" | rofi \
    -dmenu \
    -i \
    -p "Qtile Keybindings" \
    -theme-str 'window { width: 50%; }' \
    
