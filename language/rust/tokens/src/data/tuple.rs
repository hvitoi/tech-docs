// Tuples are also considered "Units" ()

fn main() {
    // Declaration tuples (with type annotations)
    let (a, b): (i32, i32);
    (a, ..) = (1, 2); // initialize only the first
    (.., b) = (1, 2); // initialize only the second

    // Destructuring
    let (mut x, mut y) = (1, 2);

    // Tuples can have multiple values
    let (a, b, c) = ('a', 'b', 'c');
}
