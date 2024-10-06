# modifies ~/.config/fish/conf.d/foo.fish
fish_add_path -U $HOME/bin
fish_add_path $HOME/bin # same as -U

# just for the current shell
fish_add_path -g $HOME/bin
