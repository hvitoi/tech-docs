# Gitlab Server

```shell
docker run --detach \
  --name "gitlab" \
  --hostname "gitlab.example.com" \
  --publish "8090:80" \
  --network "bridge" \
  --restart "always" \
  --volume "$HOME/gitlab_home/config:/etc/gitlab" \
  --volume "$HOME/gitlab_home/logs:/var/log/gitlab" \
  --volume "$HOME/gitlab_home/data:/var/opt/gitlab" \
  "gitlab/gitlab-ee:latest"
```

```shell
sudo echo -n "127.0.0.1 gitlab.example.com" >> /etc/hosts
```

## Repositories

- Repos are stored at `/var/opt/gitlab/git-data/repositories/repo-group/repo-name.git`
