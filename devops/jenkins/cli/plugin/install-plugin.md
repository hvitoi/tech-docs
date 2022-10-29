# install-plugin

- Plugin name can be an `URL` or the `shortname` in the update center

```sh
jenkinscli install-plugin "plugin-name"
jenkinscli install-plugin "ssh"
jenkinscli install-plugin "ssh" -deploy # deploy right away
jenkinscli install-plugin "ssh" -restart # restart after successful installation
```
