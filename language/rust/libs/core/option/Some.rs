fn main() {
    let five: Option<i32> = Some(5);
    let six: Option<i32> = plus_one(five);
}

fn plus_one(x: Option<i32>) -> Option<i32> {
    match x {
        None => None,
        Some(i) => Some(i + 1),
    }
}
