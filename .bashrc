#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '

if [ -f $HOME/.bashrc-personal ]; then
    source $HOME/.bashrc-personal
fi

eval "$(starship init bash)"
neofetch

