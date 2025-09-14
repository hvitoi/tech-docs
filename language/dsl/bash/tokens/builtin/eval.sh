# - Evaluates shell commands from a text input
# - Usually used to evaluate "export" commands in order to set environment variables

eval myenvs.txt

eval "$(minikube docker-env)"
eval "$(fzf --zsh)"
