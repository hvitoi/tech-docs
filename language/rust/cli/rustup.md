# rustup

- Rustup is a `toolchain management`
- Rustup home directory: `~/.rustup`
  - Can be overriden with `$RUSTUP_HOME`
- Cargo home directory: `~/.cargo`
  - Can be overriden with `$CARGO_HOME`
- Binaries directory: `~/.cargo/bin`
  - Binaries: `cargo`, `rustc`, `rustup`
  - This directory must be added to `$PATH`

## update

- Update the toolchain

```shell
rustup update
```

## self

```shell
# Uninstall everything
rustup self uninstall
```

## target

- Manage compilation targets

```shell
# List all available platform targets (architectures)
rustup target list

# Add a new target
rustup target add wasm32-unknown-unknown # web assembly
```
