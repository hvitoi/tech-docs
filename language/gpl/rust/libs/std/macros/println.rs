fn main() {
    println!("Hey!");

    let x = 1;
    println!("x: {}", x);

    // Binary
    println!("{:04b}", 10); // 4 digits binary representation of 10

    // Debug Notation (works with any type that implements the Debug trait)
    println!("{:?}", String::from("hey")); // string
    println!("{:?}", String::from("hey")); // array
    println!("{:#?}", [1, 2, 3]);

    // Pointer
    println!("memory address of x: {:p}", &x);
}
