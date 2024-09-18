# Nix Ecosystem

- **Nix**
  - The functional package manager

- **Nixpkgs**
  - The packages collection
  - The packages can be installed with the nix package manager
  - <https://github.com/NixOS/nixpkgs>

- **NixOS**
  - A Linux distribution that can be configured fully declaratively

- **Nix Language**
  - It is a domain-specific, purely functional, lazily evaluated, dynamically typed programming language

## Nix Package Manager

- Nix configuration at `/etc/nix/nix.conf`
- <https://search.nixos.org>
- <https://status.nixos.org/>
- <https://github.com/NixOS/nixpkgs>

## NixOS

### Filesystem

- **/bin**
  - Contains a single `sh` binary symlinked to nixstore
- **/etc**

### Nix Store

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
