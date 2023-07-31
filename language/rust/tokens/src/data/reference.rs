fn main() {
    // Reference
    let s1 = String::from("hey");
    let len = calculate_length(&s1); // borrows ownership

    let mut s2 = String::from("hello");
    add_more(&mut s2); // borrows ownership

    // Dereference
    let mut x: Box<i32> = Box::new(5); // ref
    *x = 4;
}

fn calculate_length(s: &String) -> usize {
    s.len() // calculate len based on the pointer
}

fn add_more(s: &mut String) {
    s.push_str("world");
}
