# Protocols

## DLNA

- For: Streaming media (video, music) over local networks.
- Use: Home media sharing to smart TVs and consoles.
- Security: Minimal, no authentication; local use only.

## Docker Volume Plugin

- For: Exposing remote storage to Docker containers.
- Use: Access cloud storage in containerized apps.
- Security: Depends on Docker settings and network isolation.

## FTP

- For: File transfers between systems.
- Use: Legacy or server environments.
- Security: Insecure by default; avoid over untrusted networks.

## HTTP

- For: Basic file sharing over HTTP.
- Use: Simple, quick file sharing via web.
- Security: No encryption; use SSL/TLS for secure access.

## NFS

- For: Sharing files over a local network.
- Use: Linux and Unix-based systems.
- Security: Limited; best on secure networks.

## Restic

- For: Serving as a storage backend for Restic backups.
- Use: Reliable, encrypted backup storage.
- Security: Requires secure network or localhost access.

## S3

- For: Serving as an S3-compatible storage endpoint.
- Use: Cloud-based object storage.
- Security: SSL/TLS recommended for secure access.

## SFTP

- For: Secure file transfers over SSH.
- Use: Remote access with encryption.
- Security: High; uses SSH for secure connections.

## WebDAV

- For: Network file sharing with broad client support.
- Use: Accessible from Finder, Windows, and many apps.
- Security: Moderate; SSL/TLS recommended for remote access.

```shell
curl -u "username:password" -X PROPFIND http://example.com/webdav/
```
