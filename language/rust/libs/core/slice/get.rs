fn main() {
    /*
        - Slice is a reference to a contiguous sequence of elements in a collection
        - Borrows part of a collection without taking ownership of the entire collection
        - From arrays, vectors, strings and other collections implementing the deref trait
    */

    let a: [char; 3] = ['a', 'b', 'c'];

    // Get by index
    let b: Option<&char> = a.get(0);
    b.unwrap();
}
