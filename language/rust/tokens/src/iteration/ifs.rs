fn main() {
    if 1 == 1 {
        println!("Correct!");
    } else {
        println!("Lie!");
    }

    // assert while assigning
    enum Message {
        Quit,
        Move { x: i32, y: i32 },
        Write(String),
        ChangeColor(i32, i32, i32),
    }
    let msg: Message = Message::Move { x: 1, y: 2 };

    // Destructuring
    if let Message::Move { x: a, y: b } = msg {
        // ensure that it's a Move variant
        print!("{}, {}", a, b);
    } else {
        panic!("Never let this run.")
    }
}
