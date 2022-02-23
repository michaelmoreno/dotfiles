#
# ~/.bashrc
#

# If not running interactively, don't do anything
[[ $- != *i* ]] && return

alias ls='ls --color=auto'
alias pacman='sudo pacman'
alias open='xdg-open'
alias riwd='sudo systemctl restart iwd'
alias cat='ccat'
alias tr='tree -C'
export PATH=$PATH:/home/mm/.local/bin
PS1='[\[\033[34m\]\u@\[\033[34m\]\h \[\033[36m\]\W\[\033[37m\]]\$ '

source $HOME/.nix-profile/etc/profile.d/nix.sh

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/mm/anaconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/mm/anaconda3/etc/profile.d/conda.sh" ]; then
        . "/home/mm/anaconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/mm/anaconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

