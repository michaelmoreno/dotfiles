if status is-interactive
    # Commands to run in interactive sessions can go here
end

# Aliases
alias dotfiles='/usr/bin/git --git-dir=$HOME/dotfiles/ --work-tree=$HOME'

# Abbreviations
abbr pacman 'sudo pacman'
abbr clip 'xclip -selection clipboard'
abbr c 'ccat'
abbr tree 'tree -C'
abbr sriwd 'sudo systemctl restart iwd.service'
abbr search 'sudo updatedb & locate'
abbr nano 'sudo nano'
abbr br 'br ~'
abbr kbrs 'setxkbmap -option caps:super && setxkbmap -option ctrl:ralt_rctrl && xset r rate 200 30'

## Programs
abbr davinci 'prime-run /opt/resolve/bin/resolve'

alias py='python'


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
