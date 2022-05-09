# Installation

## Via Snaps

`sudo apt install snapd`

`sudo snap install --classic heroku`

# Basic commands

### Version

`heroku -v`

### Login

`heroku login`

# Setup ssh keys

```bash
heroku keys:add # Look for existing keys in the computer
heroku create <app-name>  # Run inside of the app folder
```

- App: https://hvitoi.herokuapp.com/
- Repo: https://git.heroku.com/hvitoi-js-apps.git

# Setup environment variables

```bash
heroku config                       # Show all env variables
heroku config:set <key=value>       # Add env variable
heroku config:unset <key>           # Remove env variable
```

# Push to keroku

```bash
git init
git status
git add .
git commit -m "First push to heroku"
git push origin master  # pushes to github!
git push heroku master  # pushes to heroku!
```
