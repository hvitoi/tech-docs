fn main() {
    /*
        - Slice sizes are not known at compile time
        - Borrow a section of an array
    */

    // Slice of chars
    let arr: [i32; 3] = [1, 2, 3];
    let a: &[i32] = &arr[0..2]; // index 0 and 1
    let b: &[i32] = &arr[..2]; // index 0 and 1
    let c: &[i32] = &arr[1..]; // index 1 and 2
}
