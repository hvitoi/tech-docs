# bash

```shell
bash -c "sleep 1 && echo hello"
bash -l # or bash --login -> starts bash as login shell - reads the login initialization files (~/.bash_profile, /etc/profile) instead of just ~/.bashrc. Useful when you need the full login environment but you're already inside a session — e.g. in a script that needs the same env vars set up by your login config.
```
