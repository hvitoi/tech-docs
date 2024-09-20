# Nix Ecosystem

- Written in 2003 by Eelco Dolstra in his PhD thesis
- <https://status.nixos.org/>
- <https://search.nixos.org>
- <https://nixos.org/manual/nixos/>
- <https://nix.dev/>

## Pieces

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

- <https://github.com/NixOS/nixpkgs>

## NixOS

- Available NixOS options: <https://search.nixos.org/options>

### Filesystem

- **/bin**
  - Contains a single `sh` binary symlinked to nixstore
- **/etc**

### Nix Store

- Packages are installed at `/nix/store/`
- Each path has a unique SHA-256 hash

```txt
├── /nix/store/lgr3n0573wi478bj456zggh541wjrbiw-git-2.46.0
│   ├── bin
│   ├── lib
│   ├── libexec
│   ├── share
│   └── scalar
```

- NixOS installed packages are also located at nix-store, but symlinked to `/run/current-system/sw/`
