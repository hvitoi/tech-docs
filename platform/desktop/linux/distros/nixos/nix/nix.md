# Nix

- Nix configuration at `/etc/nix/nix.conf`

## Packages

- <https://search.nixos.org/packages>
- <https://github.com/NixOS/nixpkgs>
- Packages are installed at `/nix/store/`

```txt
├── /nix/store/lgr3n0573wi478bj456zggh541wjrbiw-git-2.46.0
│   ├── bin
│   ├── lib
│   ├── libexec
│   ├── share
│   └── scalar
```

- `nix-shell` references the files directly from nix-store
- NixOS installed packages are also located at nix-store, but symlinked to `/run/current-system/sw/`
