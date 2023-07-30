fn main() {
    // let: immutable variable!
    let a: i32 = 5; // declaration with type annotation and initialization
    let a = "hello"; // it can be declared again and with another type! It shadows the first one
    let _b: i32; // declaration only (unused warning and be ignore with the _). Or #[allow(unused_variables)] annotation
    let c = 5; // type infer
    let c = 'a';

    // let mut: mutable variable!
    let mut d = 1;
    d += 2;
    d = d + 2;

    // type annotations
    let e: i32; // signed integer (default) - 8, 16 (short), 32 (normal), 64 (long), 128 bits
    let f: u32; // unsigned integer - 8, 16 (short), 32 (normal), 64 (long), 128 bits

    // arch sizes match the size of a "word" (how many bytes the computer reads at a time) - 32 bits (4 bytes), 64 bits (8 bytes)
    let g: isize; // signed integer (depends on the architecture - e.g., 32 vs 64)
    let h: usize; // unsigned integer (depends on the architecture - e.g., 32 vs 64)

    let i: f64; // float (default) - 32 or 64

    let z: &str; // string
}
