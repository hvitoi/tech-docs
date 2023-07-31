fn main() {
    // Allocates an integer on the heap
    // X holds then a pointer instead
    let mut x: Box<i32> = Box::new(5);

    *x = 4;
}
