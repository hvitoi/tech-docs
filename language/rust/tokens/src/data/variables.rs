fn main() {
    // let: immutable variable!
    let a: i32 = 5; // declaration with type annotation and initialization
    let a = "hello"; // it can be declared again and with another type! It shadows the first one
    let _b: i32; // declaration only (unused warning and be ignore with the _). Or #[allow(unused_variables)] annotation
    let c = 5; // type infer

    // let mut: mutable variable!
    let mut d = 1;
    d += 2;
    d = d + 2;
}
