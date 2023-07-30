use std::ops::{Range, RangeInclusive};

fn main() {
    // Range (0 to 9)
    for i in 0..10 {
        println!("{}", i);
    }
    for i in (Range { start: 0, end: 10 }) {
        println!("{}", i);
    }

    // Range Inclusive (a to z)
    for i in 0..=5 {
        println!("{}", i);
    }
    for i in (Range {
        start: 'a',
        end: 'z',
    }) {
        println!("{}", i);
    }

    for c in 'a'..='z' {
        println!("{}: {}", c, c as u8);
    }
}
