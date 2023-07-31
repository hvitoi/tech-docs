fn main() {
    struct Person {
        name: String,
        age: Box<u8>,
    }

    let henry = Person {
        name: String::from("Henry"),
        age: Box::new(29),
    };

    // Destructure Struct
    // `name` is moved out of person, but `age` is referenced
    let Person { name, ref age } = henry;

    println!("name: {}, age: {}", name, age);
    // println!("age: {}", henry.name); // fail! (ownership was taken)
    println!("age: {}", henry.age); // ok! (ownership was not taken)
}
