/*
    - In a lo
*/

fn main() {
    // let mut sum: i32;

    // from 0 to 4
    for i in 0..5 {
        println!("{}", i);
    }

    // from 0 to 5
    for i in 0..=5 {
        if i == 2 {
            // skip on 2
            continue;
        }
        if i == 4 {
            // break out on 4
            break;
        }
        println!("{}", i);
    }

    // from a to z
    for c in 'a'..='z' {
        println!("{}: {}", c, c as u8);
    }

    // from string
    for i in "Henrique".chars() {
        println!("{}", i);
    }

    // from array
    let arr1: [String; 2] = [String::from("a"), String::from("b")];
    for el in arr1 {
        // takes ownership
        println!("{}", el);
    }
    // println!("{:?}", arr1); // won't work because the ownership has been taken by the for loop

    let arr2: [String; 2] = [String::from("a"), String::from("b")];
    for el in &arr2 {
        // doesn't take ownership
        println!("{}", el);
    }
    println!("{:?}", arr2);

    let arr3: [char; 2] = ['a', 'b'];
    for el in arr3 {
        // ownership here doesn't matter because the string literal is copied
        println!("{}", el);
    }

    /*
       - index & value iteration
    */
    for (i, v) in ['a', 'b', 'c'].iter().enumerate() {
        println!("{}: {}", i, v)
    }
}
