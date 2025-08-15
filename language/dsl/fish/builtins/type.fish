# Returns 0 if the command exists as a command, builtin or function
type -q fish

# command -q, which will return 0 only if it exists as an external program
# builtin -q, which will return 0 only if it is a fish builtin
# functions -q, which will return 0 only if it is a fish function
