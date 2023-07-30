fn just_print() {
    // The compiler infers the return type
    // In this case the return type is an empty Unit ()
    println!("Hey!");
}

fn sum(x: i32, y: i32) -> i32 {
    x + y // expression!
}

fn never_return() -> ! {
    // Diverging functions (never return to the caller)
    panic!();
}

fn main() {
    just_print();
    println!("{}", sum(1, 2));
    // never_return();
}
