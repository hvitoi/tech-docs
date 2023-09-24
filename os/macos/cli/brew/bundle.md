# bundle

- When running for the first time, it will automatically setup add the tap `homebrew/bundle`
- Brew files must be placed at `~/.config/brewfile/Brewfile`

```shell
# Extract the current packages into a Brewfile
brew bundle dump --describe

# Install/Upgrade all apps listed in Brewfile
brew bundle install
brew bundle install --global # use Brewfile from ~/.Brewfile

# Uninstall all apps not listed in Brewfile
brew bundle cleanup

# Check if Brewfile reflects the current state
brew bundle check
```
