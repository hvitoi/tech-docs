/*
    - Group together different data types
    - Similar to tuples, but each value has a name (not a position)
*/

fn main() {
    #[derive(Debug)] // Implement the Debug trait to make a struct printable
    struct Person {
        name: String,
        age: Box<u8>,
    }

    let age: Box<u8> = Box::new(29);
    let henry: Person = Person {
        name: String::from("Henry"),
        age, // use for the field the value of a variable with same name
    };

    // Struct Update Syntax
    let updated_henry: Person = Person {
        name: henry.name,
        age: Box::new(30),
    };

    let updated_again_henry: Person = Person {
        age: Box::new(31),
        ..updated_henry
    };

    // Destructure Struct
    // `name` is moved out of person, but `age` is referenced
    let Person { name, ref age } = updated_again_henry;

    println!("name: {}, age: {}", name, age);
    // println!("age: {}", henry.name); // fail! (ownership was taken)
    println!("age: {}", henry.age); // ok! (ownership was not taken)

    // Tuple Structs
    struct Color(i32, i32, i32);
    struct Point(i32, i32, i32);
    let black = Color(0, 0, 0);
    let origin = Point(0, 0, 0);

    // Unit-Like Structs (struct without any field)
    struct Unit;
    // impl SomeTrait for Unit {}
    let u = Unit;
}
