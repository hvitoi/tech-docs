# rsync

- Utility for transferring and synchronizing files within same computer or to a remote computer
- Compares the modification time and size of the files
- Rsync is a lot faster than ftp or scp
- Used mostly to `backup` files
- Port `22` (same as SSH)
- Rsync uses SSH to transfer the files!

```shell
rsync -zvh "/local/source/file.txt" "/local/destination/folder" # Local file sync
rsync -azvh "/local/source/folder" "/local/destination/folder" # Local directory sync

rsync -avz "/local/source/file.txt" "user@ip:/remote/destination/folder" # Push to remote server
rsync -avzh "user@ip:/remote/source/file.txt" "/local/destination/folder" # Pull from remote server

# Local sync
tar -cvf backup.tar /home/hvitoi
mkdir /tmp/backups
rsync -zvh /home/hvitoi/backup.tar /tmp/backups # sync the file in the home and backups dirs
rsync -azvh /home/hvitoi/hvitoi /tmp/backups  # sync the folder

# Remote sync
mkdir /tmp/backups # folder on remote server
rsync -avz /home/localfile hvitoi@192.168.1.30:/home/hvitoi/remote/folder # sync file to remote server
rsync -avzh hvitoi@192.168.1.30:/home/hvitoi/serverfile /home/local/folder
```
