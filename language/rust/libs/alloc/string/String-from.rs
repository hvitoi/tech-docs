fn main() {
    // holds pointer, length and capacity
    let mut a: String = String::from("hello");
    // stack size: 3 * usize (8 usually - 64 bits) = 24 bytes - 1 byte for pointer, 1 byte for length, 1 byte for capacity
    // heap size: 5 * char (4 bytes) =  20 bytes

    // Concatenate a string slice
    a += " world!";

    // Convert to a string slice
    let b: &str = &a;
    let c: &str = a.as_str(); // also works
}
