# NixOS

## Filesystem

- **/bin**
  - Contains a single `sh` binary symlinked to nixstore
- **/etc**

## Nix Store

- Packages are installed at `/nix/store/`

```txt
├── /nix/store/lgr3n0573wi478bj456zggh541wjrbiw-git-2.46.0
│   ├── bin
│   ├── lib
│   ├── libexec
│   ├── share
│   └── scalar
```

- NixOS installed packages are also located at nix-store, but symlinked to `/run/current-system/sw/`
