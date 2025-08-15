# cargo

## run

```shell
cargo run
```

## install

```shell
# builds the project in the current folder
# installs it into ~/.cargo/bin/<project-name> and ./target/release/<project-name>
cargo install --path "."
```

## build

```shell
cargo build
cargo build --locked --release
```

## test

```shell
cargo test --locked
```

## fmt

- Format

```shell
cargo fmt -- --check
```

## clippy

```shell
cargo clippy -- -Dwarnings
```

## new

```shell
cargo new "folder"
```

## init

- Like `new`, but for an existing folder

```shell
cargo new "folder"
```
