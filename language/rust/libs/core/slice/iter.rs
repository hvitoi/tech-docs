/*
    - Create an iterator out of a collection
*/

fn main() {
    for (i, v) in ['a', 'b', 'c'].iter().enumerate() {
        println!("{}: {}", i, v)
    }
}
