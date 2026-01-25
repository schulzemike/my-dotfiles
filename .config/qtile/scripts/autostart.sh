#!/bin/bash

function run_once {
  if ! pgrep -x $(basename $1 | head -c 15) 1>/dev/null;
  then
    $@&
  fi
}

run_once sxhkd -c ~/.config/sxhkd/sxhkdrc &

# autostart the XDG desktop entries
# especially the VBoxClinent all - script for clipboard, ...
# see: /etc/xdg/autostart
run_once dex -a

# autostart flameshot
run_once flameshot

