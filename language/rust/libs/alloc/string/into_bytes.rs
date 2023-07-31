fn main() {
    let s = String::from("hey");

    // s is consumed and can't be used anymore
    // ownership is moved to ss
    let ss = s.into_bytes(); // vector of bytes

    assert_eq!(&[104, 101, 121][..], &ss[..]);
}
