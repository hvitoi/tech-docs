/*
    - A set of possible values
    - Useful in match statements
    - Each item in an enum is an "variant"
*/

fn main() {
    enum IpAddr {
        V4(String), // implicitly takes value 0
        V6(String), // implicitly takes value 1
    }

    let home = IpAddr::V4(String::from("127.0.0.1")); // uses the variant V4
    let loopback = IpAddr::V6(String::from("::1")); // uses the variant V6

    enum MyNumber {
        Ten = 10, // explicitly defines value
        Twelve = 20,
        Thirdy = 30,
    }

    enum MyNumberr {
        Six = 6, // explicitly defines value
        Seven,   // implicitly takes 7
        Eight,   // ...
    }

    // Cast enum
    assert_eq!(MyNumber::Ten as u8, 10);

    // Enums with additional information
    enum Message {
        Quit,
        Move { x: i32, y: i32 },
        Write(String),
        ChangeColor(i32, i32, i32),
    }
    let msg1: Message = Message::Quit;
    let msg2: Message = Message::Move { x: 1, y: 2 };
    let msg3: Message = Message::Write(String::from("hello"));

    // Destructuring
    if let Message::Move { x: a, y: b } = msg2 {
        // ensure that it's a Move variant
        print!("{}, {}", a, b);
    } else {
        panic!("Never let this run.")
    }
}
