# Configure SSH

```sh
# List existing keys
ls ~/.ssh

# Create the SSD key-pair
ssh-keygen -t rsa -b 4096 -C "hvitoi@gmail.com"
# -t (type): rsa protocol
# -b (bits): bits fr the key
# -C: label/comment

- Must be run in ~/.ssh
- Accept defaults
- id_rsa (secret file and never share)
- id_rsa.pub (share with github and heroku)

# Start the ssh-agent in background (and print the process id)
eval "$(ssh-agent -s)"

# Register the SSH key
ssh-add -K ~/.ssh/id_rsa

# Add SSH key to GitHub/Gitlab -> Settings/SSH
- Title: Personal Laptop
- Key: Content of `~/.ssh/id_rsa.pub`

# Test github connection
ssh -T git@github.com # Accept 'yes'
```
