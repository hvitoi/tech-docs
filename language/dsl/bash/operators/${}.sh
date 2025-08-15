# - Parameter expansion <https://pubs.opengroup.org/onlinepubs/9699919799/utilities/V3_chap02.html#tag_18_06_02>

## ${#parameter}
# - Length of the parameter
BAR=("alpha" "beta" "gamma")
echo ${#HEY}

FOO="abcd"
echo ${#FOO}

## ${parameter[n]}
# - Get element in nth position
BAR=("alpha" "beta" "gamma")
echo "${BAR[0]}" # first element
echo "${BAR[@]}" # all elements
echo "${BAR[*]}" # all elements

## ${parameter%word}
# - Removes `suffix` matching the `last occurrence`
FOO='my-package-git'
echo ${FOO%-git} # my-package

# removes everything after "/" (inclusive)
FOO='a/b/c'
echo ${FOO%/*} # a/b

## ${parameter%%word}
# - Removes `suffix` matching the `first occurrence`
FOO='a/b/c'
echo ${FOO%%/*} # a

VERSION=12.5.7
MAJOR=${VERSION%%.*}
echo "$MAJOR" # 12

## ${parameter#[word]}
# - Removes `prefix` matching the `last occurrence`
FOO='my-package-git'
echo ${FOO#my-} # package-git

FOO='card2-eDP-1'
echo ${FOO#card?-}

GITHUB_REF=refs/heads/main
tag=${GITHUB_REF#refs/tags/}
echo "$tag"

## ${parameter##[word]}
# - Removes `prefix` matching the `first occurrence`
FOO='11package11'
echo ${FOO##11} # package11

## ${parameters:-[word]}
# - Use default value
FOO=''
echo "${FOO:-nothing}" # "nothing" if FOO is undefined or null

# optional second parameter (fallback to logfile)
output_file=${2:-logfile}
echo "$output_file"

## ${parameters-[word]}
# - Fallback
FOO=''
echo "${FOO-nothing}" # "nothing" if FOO is undefined

## ${parameters:=[word]}
# - Assign default value
FOO=''
echo "${FOO:=nothing}" # "nothing" if FOO is undefined or null

## ${parameters+[word]}
# - If parameter is set, return the evaluation of the word
# - If parameter is not set, returns null
${parameter+[word]}

${FOO+whoami}

## ${parameters:?[word]}
# - Abort (non-zero exit) if a given variable is unset or null
echo "${HOME:?}/awesome/"

# Required first parameter
input_file=${1:?usage: $0 input_file}
echo "$input_file"

## ${parameters::-n}
# - Remove last n characters

FOO='bar'
echo "${FOO::-1}" # ba
