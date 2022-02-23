if status is-interactive
    # Commands to run in interactive sessions can go here
end

# Aliases
alias dotfiles='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'

# Abbreviations
abbr clip 'xclip -selection clipboard'
abbr c 'ccat'

set fish_color_normal normal
set fish_color_command --bold
set fish_color_param cyan
set fish_color_redirection brblue
set fish_color_comment red
set fish_color_error brred
set fish_color_escape bryellow --bold
set fish_color_operator bryellow
set fish_color_end brmagenta
set fish_color_quote yellow
set fish_color_autosuggestion 555 brblack
set fish_color_user brgreen


# Start X at login
if status is-login
    if test -z "$DISPLAY" -a "$XDG_VTNR" = 1
        exec startx -- -keeptty
    end
end
