fn main() {
    let num = 5;
    if num > 0 {
        println!("Positive.");
    } else if num < 0 {
        println!("Negative.");
    } else {
        println!("Zero.");
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

    let five: Option<i32> = Some(5);
    if let Some(n) = five {
        println!("The number is {}.", n);
    } else {
        println!("No number found.");
    }

    /*
        If-else conditionals inside of let
    */

    let num: i32 = 5;
    let big_n: i32 = if num < 10 && num > -10 {
        10 * num
    } else {
        num / 2
    };
}
