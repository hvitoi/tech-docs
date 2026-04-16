# gh pr

## view

```shell
gh pr view 40640 --repo hvitoi/foo
```

## create

```shell
gh pr create --title "add aws-devops-agent addon and EKS auth mapping" --body "$(cat <<'EOF'
## 🤔 Problem

Solving this

## 🧐 Solution

- Changes this

## ✔️ Checklist to merge

- [x] Awesome
EOF
)"
```

## edit

```shell
gh pr edit 40640 --repo hvitoi/foo --body "## Context

My new PR description"
```
