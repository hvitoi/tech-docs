fn main() {
    let x = u8::checked_add(254, 1).unwrap();
    println!("{}", x);

    // let x = u8::checked_add(255, 1).unwrap(); // this would throw
}
