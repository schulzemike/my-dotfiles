#!/usr/bin/env bash

# Define options
options="Config Files\nLogs"

# Call first menu
choice=$(echo -e "$options" | rofi -dmenu -p "System" -theme-str 'element-icon { enabled: false; }')
# Handle selection and call nested menus
case "$choice" in
    "Config Files")
        # Call a second rofi menu or script
        ~/.config/rofi/scripts/open-config.sh
        ;;
    "Logs")
        # Call another menu
        ~/.config/rofi/scripts/open-log.sh
        ;;
esac
