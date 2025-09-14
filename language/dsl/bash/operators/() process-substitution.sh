# Process substitution

diff /etc/hosts <(ssh somehost cat /etc/hosts)
ssh somehost cat /etc/hosts | diff /etc/hosts # same!

# --

my_hosts=$(
  cat <<'EOF'
example.com
localhost
EOF
)
diff /etc/hosts <(echo "$my_hosts")
