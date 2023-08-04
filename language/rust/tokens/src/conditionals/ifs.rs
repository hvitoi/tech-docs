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
        ChangeColor(u8, u8, u8),
    }
    let msg1: Message = Message::Move { x: 1, y: 2 };
    let msg2: Message = Message::ChangeColor(255, 255, 255);

    /*
       If Let destructuring
       It's this truthy if the destructuring can happen successfully
    */
    if let Message::Move { x: a, y: b } = msg1 {
        // ensure that it's a Move variant
        println!("{}, {}", a, b);
    } else {
        panic!("")
    }

    if let Message::ChangeColor(a, b, c) = msg2 {
        // ensure that it's a Move variant
        println!("{}, {}, {}", a, b, c);
    } else {
        panic!("")
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
