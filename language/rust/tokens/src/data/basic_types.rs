fn main() {
    // Integer
    let e: i32; // signed integer (default) - 8, 16 (short), 32 (normal), 64 (long), 128 bits
    let f: u32; // unsigned integer - 8, 16 (short), 32 (normal), 64 (long), 128 bits

    // arch sizes match the size of a "word" (how many bytes the computer reads at a time) - 32 bits (4 bytes), 64 bits (8 bytes)
    let g: isize; // signed integer (depends on the architecture - e.g., 32 vs 64)
    let h: usize; // unsigned integer (depends on the architecture - e.g., 32 vs 64)

    // Float
    let i: f64; // float (default) - 32 or 64

    // String
    // stack size: 3 * usize (8 usually - 64 bits) = 24 bytes - 1 byte for pointer, 1 byte for length, 1 byte for capacity
    // heap size: 5 * char (4 bytes) =  20 bytes
    let z = String::from("hello"); // holds pointer, length and capacity
    let z: &str = "hello"; // holds only the pointer

    // Char
    let c: char = 'a'; // 4 bytes! Holds every unicode symbol

    // Boolean
    let h: bool = true; // 1 byte

    // Units
    let i: () = (); // 0 byte (Unit is the base for tuples)
    let j: (char) = ('a'); // Redundant! The parentesis could be removed
    let k: (char, char) = ('a', 'b'); // Actual tuple
}
