fn main() {
    /*
        - Fixed-size collection of elements
        - Same data type
        - Contiguous block in stack memory
    */

    // Size defined beforehand
    let a: [char; 3] = ['a', 'b', 'c'];
    let b: [_; 3] = ['a', 'b', 'c']; // compiler infers the data type
    let c = ['a', 'b', 'c']; // compiler infers everything
    let d: [i32; 100] = [1; 100]; // [1, 1, 1, ..., 1]

    // Access
    assert!(a[0] == 'a');
    assert!(a.get(0).unwrap() == &'a');
    // a[9] == 'a'; // panics, out of borders index

    // Destructure array
    let [alpha, ..] = ['a', 'b', 'c']; // destructure only the first element
    println!("{}", alpha);
}
