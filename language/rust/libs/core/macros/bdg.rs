fn main() {
    // Prints debug information to the sterr
    let foo = "bar";
    dbg!(foo); // prints to stderr
    println!("{}", foo); // perints to stdout
}
