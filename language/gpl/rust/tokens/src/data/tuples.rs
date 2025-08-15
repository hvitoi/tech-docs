/*
    - Tuples are also considered "Units" ()
    - Collection of different types
    - Contiguous block of memory in the stack
*/

fn main() {
    // Tuples can have multiple values
    let t1: (i32, char, char) = (5, 'b', 'c');

    // Nested tuple
    let t2: (i32, (i32, i32)) = (0, (0, 0));

    // Access
    let t = (String::from("hey"), String::from("hello"));
    println!("{}", t.0);
    println!("{}", t.1);

    // Destructuring
    // let (a, b) = (1, 1);
    let (a, b): (i32, char); // declaration
    (a, ..) = (1, "aaa"); // initialize only the first
    (.., b) = ("aaa", 'z'); // initialize only the second
    let (mut x, mut y) = (1, 2);
}
