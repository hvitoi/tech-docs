fn main() {
    // Tuples
    let (x, y) = (1, 2);

    // Struct
    struct Person {
        name: String,
        age: Box<u8>,
    }

    let henry = Person {
        name: String::from("Henry"),
        age: Box::new(29),
    };

    let Person { name, age } = henry;
}
