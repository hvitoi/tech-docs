fn main() {
    // Give ownership
    let x = String::from("foo"); // size unknown at compile-time
    takes_ownership(x);
    // println!("{}", a_string); // Not possible (ownership has been moved)

    // Copy ownership
    let x = 5; // size known at compile-time
    copies_ownership(x);
    println!("{}", x); // Possible! (ownership has been copied)

    // Receive ownership
    let x = gives_ownership();

    // Give and receive back ownership
    let x = takes_and_gives_back_ownership(x);
}

fn takes_ownership(a: String) {
    println!("{}", a);
}

fn copies_ownership(a: i32) {
    println!("{}", a);
}

fn gives_ownership() -> String {
    let a = String::from("foo");
    println!("{}", a);
    a
}

fn takes_and_gives_back_ownership(a: String) -> String {
    println!("{}", a);
    a
}
