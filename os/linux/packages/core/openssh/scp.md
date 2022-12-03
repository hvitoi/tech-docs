# scp

- Secure Copy Protocol (SCP)
- Similar to FTP, but with security and authentication added
- Port `22` (same of ssh)

```shell
scp -i "key.pem" "user@host:/remote/file-src.txt" "/local/directory/dest" # copy txt from server to local dest folder
```
