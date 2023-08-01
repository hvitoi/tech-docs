fn main() {
    println!("Hey!");

    let x = 1;
    println!("x: {}", x);

    // Binary
    println!("{:04b}", 10); // 4 digits binary representation of 10

    // String
    println!("{:?}", String::from("hey"));

    // Pointer
    println!("memory address of x: {:p}", &x);
}
