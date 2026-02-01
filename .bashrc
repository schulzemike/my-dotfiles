#
# ~/.bashrc
#

set -o vi
HISTSIZE=5000


# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

if [ -f $HOME/.bashrc-personal ]; then
    source $HOME/.bashrc-personal
fi

if [ -f $HOME/.bashrc-work ]; then
    source $HOME/.bashrc-work
fi

eval "$(starship init bash)"
fastfetch



#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="/home/mike/.local/sdkman"
[[ -s "/home/mike/.local/sdkman/bin/sdkman-init.sh" ]] && source "/home/mike/.local/sdkman/bin/sdkman-init.sh"


