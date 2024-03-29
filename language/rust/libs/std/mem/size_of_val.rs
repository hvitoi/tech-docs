use std::mem::size_of_val;

fn main() {
    // Chars have 4 bytes
    let a: char = 'a';
    assert_eq!(size_of_val(&a), 4);

    // Int8 have 1 byte
    let b: i8 = 9;
    assert_eq!(size_of_val(&b), 1);

    // Boolean has 1 byte
    let c: bool = true;
    assert_eq!(size_of_val(&c), 1);

    // Array of chars
    let d: [char; 3] = ['a', 'b', 'c'];
    assert_eq!(size_of_val(&d), 12);

    // Slice
    let e = &d[..]; // each element occupies usize given that it's a pointer
    assert_eq!(size_of_val(&e), 16);
}
