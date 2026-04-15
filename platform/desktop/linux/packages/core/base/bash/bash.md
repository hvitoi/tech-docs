# bash

```shell
bash -c "sleep 1 && echo hello"

# starts bash as login shell - reads the login initialization files (~/.bash_profile, /etc/profile) instead of just ~/.bashrc. Useful when you need the full login environment but you're already inside a session — e.g. in a script that needs the same env vars set up by your login config.
bash -l # or bash --login

# forces bash to start in interactive mode even if it wouldn't normally be — e.g. when running a script that needs a prompt or when stdin isn't a terminal. Sometimes happens that when exec-ing on docker bash won't auto detect interactive mode
bash -i
```
