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

export DOCKER_HOST=unix://$XDG_RUNTIME_DIR/docker.sock

