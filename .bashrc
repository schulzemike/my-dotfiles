#
# ~/.bashrc
#

# load secrets already at login - so that tools that use environment variables can use them
[[ -f ~/.bashrc-secret ]] && . ~/.bashrc-secret

set -o vi
HISTSIZE=5000


# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

[[ -f ~/.bashrc-personal ]] && . ~/.bashrc-personal
[[ -f ~/.bashrc-work ]] && . ~/.bashrc-work

eval "$(starship init bash)"



#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="/home/mike/.local/sdkman"
[[ -s "~/.local/sdkman/bin/sdkman-init.sh" ]] && . ~/.local/sdkman/bin/sdkman-init.sh


