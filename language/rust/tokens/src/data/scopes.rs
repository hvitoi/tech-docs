fn main() {
    let a = 1; // available in the whole function scope
    {
        let b = 2; // available only inside of this scope
        println!("a: {}, b: {}", a, b)
    }

    // shadowing
    let x = 1;
    println!("{}", x); // prints 1
    {
        let x = 2;
        println!("{}", x); // prints 2
    }
}
