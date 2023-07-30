fn main() {
    // let mut sum: i32;

    // from 0 to 4
    for i in 0..5 {
        println!("{}", i);
    }

    // from 0 to 5
    for i in 0..=5 {
        println!("{}", i);
    }

    // from a to z
    for c in 'a'..='z' {
        println!("{}: {}", c, c as u8);
    }
}
