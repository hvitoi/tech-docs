fn main() {
    let x = 'b';

    match x {
        'a' => {
            print!("hey!");
        }

        // else case
        _ => {
            print!("hello!");
        }
    };

    // match as an expression
    let foo: &str = match x {
        'a' | 'b' | 'c' => "lala", // discrete values
        'd'..='z' => "lili",       // range
        _ => "lele",               // else case
    };

    /*
       Destructuring
    */
    let foo: Option<u8> = Some(3);
    match foo {
        Some(n) if n > 10 => assert!(n >= 10), // match guard
        Some(n) => assert!(n < 10),
        _ => (),
    }
    struct Point {
        x: i32,
        y: i32,
    }
    let p = Point { x: 10, y: -10 };
    match p {
        Point {
            x, // same as "x: x"
            y: yy @ 0, // y must be 0
               // y: 0, // y must be 0 (but do not assign anything)
        } => println!("x={}, y={}", x, yy),
        Point {
            x: 0..=5,              // x in a range
            y: y @ (10 | 20 | 30), // destructure Y and verify if it matches the pattern
        } => println!("x={}, y={}", x, y),
        Point { x, y } => println!("x={}, y={}", x, y), // don't match pattern anything, just destructure
        _ => (),
    }

    /*
       Enums
    */
    enum Direction {
        East,
        West,
        North,
        South,
    }
    let dire: Direction = Direction::South;
    match dire {
        Direction::East => println!("East!"),
        Direction::South | Direction::North => {
            println!("South or North!");
        }
        _ => println!("West!"),
    }

    /*
       Tuple
    */
    let numbers = (2, 4, 6, 8);
    match numbers {
        (first, .., last) => println!("{} {}", first, last),
    }

    /*
       Mutable values
    */
    let mut v: String = String::from("hello, ");
    let r: &mut String = &mut v;

    match r {
        val => val.push_str(" world!"),
    }
}
