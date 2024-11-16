status --is-interactive; and rbenv init - fish | source

if command -q fzf
    fzf --fish | source
end
