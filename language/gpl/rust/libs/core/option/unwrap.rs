fn main() {
    let x = u8::checked_add(254, 1).unwrap();
    println!("{}", x);
}
