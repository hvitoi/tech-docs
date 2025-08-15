/*
    Generate key-value tuples out of a iterator
*/

fn main() {
    for (i, v) in ['a', 'b', 'c'].iter().enumerate() {
        println!("{}: {}", i, v)
    }
}
