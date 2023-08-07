/*
    Similar to interfaces/protocols
*/

fn main() {
    trait Animal {
        // Signature
        fn sound(&self) -> String;

        // Signature + Default implementation
        fn say_hi(&self) -> String {
            String::from("hi")
        }
    }

    struct Sheep;
    struct Cow;

    impl Animal for Sheep {
        fn sound(&self) -> String {
            String::from("Maah")
        }
    }

    impl Animal for Cow {
        fn sound(&self) -> String {
            String::from("Mooh")
        }
    }

    // Derivable Traits (traits implemented automatically by the compiler)
    // Debug, Clone, Copy, PartialEq
    #[derive(PartialEq, PartialOrd)]
    struct Centimeters(f64);

    // Traits as parameters
    fn notify(animal: &impl Animal) {
        // Accepts any type that implements the Summary trait
        println!("breaking new! {}", animal.sound());
    }

    // Trait Bounds
    fn notify2<T: Animal>(item: &T) {
        // same as the example above
        println!("breaking new! {}", item.sound());
    }

    // Trait Bounds (multiple)
    use std::fmt::Debug;
    use std::fmt::Display;
    fn foo<T: Display + Clone, U: Clone + Debug>(x: &T, y: &U) -> i32 {
        // T must implement Display and Clone
        // U must implement Clone and Debug
        42
    }

    // Trait Bounds with Where clause
    fn foo2<T, U>(x: &T, y: &U) -> i32
    where
        T: Display + Clone,
        U: Clone + Debug,
    {
        42
    }

    // Trait Objects

    // Trait as return type
    // fn random_animal(random_number: i32) -> impl Animal {
    //     if random_number > 0 {
    //         Sheep
    //     } else {
    //         Cow
    //     }
    // }
}
