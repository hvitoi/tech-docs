fn main() {
    let s1 = String::from("hello");
    let s2 = s1; // s1 ownership is dropped (s1 is dropped)
    let s3 = s2.clone(); // force copy (both ownerships are kept)
                         // expensive operation!
}
