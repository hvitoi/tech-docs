# Web Assembly (WASM)

- Low level language similar to assembly
  - Other languages compile to web assembly (just like it's compiled for cpu architectures)
  - It's not written directly, but used as a compilation target
  - The compiled target has extension `.wasm`
- Can be run on browsers

## Language Support

### emscripten (C/C++)

```c
// compile the js wrapper + wasm binary
emcc myapp.c

// specify output name
emcc myapp.c -o "wrapper.js"

// specify environment variables
emcc myapp.c -s "NO_EXIT_RUNTIME=1" -s "EXPORTED_RUNTIME_METHODS=ccall,cwrap" // invoke exported variables with "Module.ccall(<functionName>, <returnType>, <[argumentsTypes]>, <[arguments]>)"
```

### assemblyscript (JS/TS)

- `JS/TS`: assemblyscript

### wasm-pack (Rust)

- Libraries: `externref` and `yew`

```shell
cargo install wasm-pack
cargo install cargo-generate
```

```shell
# add build target to wasm
rustup target add wasm32-unknown-unknown
```

## Runtime

- Browsers!

### Wrapping

- WebAssembly execution can be wrapped by a javascript script

```html
<html>
  <head>
    <script>

      var exports;
      WebAssembly.instantiateStreaming(
        fetch('myapp.wasm'), {}
      ).then(results => exports = results.instance.exports);

      function run_wasm() {
        var sum = exports.sumOfNInts(9);
        console.log(sum);
      }

    </script>
  </head>
</html>
```

### Streaming

- WebAssembly execution can be wrapped by a javascript script and stream the wasm code directly

```html
<!DOCTYPE html>
<html>
  <head>
    <title>Hello World</title>
  </head>
  <body>
     <script src="a.out.js"></script>
  </body>
</html>
```
