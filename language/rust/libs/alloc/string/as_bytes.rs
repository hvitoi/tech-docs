fn main() {
    let s = String::from("hey");

    // similar to into_bytes, but the ownership is copied
    let ss = s.as_bytes(); // vector of bytes
}
