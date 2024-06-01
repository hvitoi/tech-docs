# tap

- Taps are formula and cask repositories
- The default tap is `homebrew/core`
- The simplest way to create your own formula is to create a GitHub repository called `homebrew-<something>`; put your formula file in it; then type brew tap `<username>/<something>`

```shell
# list repos
brew tap

# add repo
brew tap "user/repo" "https://github.com/user/homebrew-repo"
brew tap "homebrew/core"
brew tap "homebrew/services"
```
