# << (heredoc)
# - Multiline text in shell
# - Allows redirection of multiple lines of input as if from a file

cat <<EOF
{
  "comment":"Hey there!",
  "description": "This is a hey there!"
}
EOF

cat <<EOF >letters.txt
a
b
c
d
EOF

cat >~/file.txt <<EOL
[default]
foo = $FOO
EOL
