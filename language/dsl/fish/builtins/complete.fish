complete \
    --command aws \
    --arguments '(begin; set -lx COMP_SHELL fish; set -lx COMP_LINE (commandline); aws_completer | sed \'s/ $//\'; end)' \
    --no-files
