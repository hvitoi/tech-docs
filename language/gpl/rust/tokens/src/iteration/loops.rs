/*
    Similar to while, but it does not have a exit condition
    Instead, it must be explicitly broken out
*/

fn main() {
    let mut count: u32 = 0 as u32;

    loop {
        if count == 3 {
            println!("three");
            count += 1;
            continue;
        }

        if count == 10 {
            println!("done!");
            break;
        }

        println!("{}", count);
        count += 1;
    }

    // Break out with a value
    count = 0;
    let foo: u32 = loop {
        if count == 10 {
            break count * 2;
        }
        count += 1;
    };
    println!("{}", foo);

    // loops with labels
    let mut number1: u8 = 0;
    let mut number2: u8 = 0;
    'loop1: loop {
        'loop2: loop {
            number2 += 1;
            println!("{} {}", number1, number2);
            if number2 >= 10 {
                number2 = 0;
                break 'loop2;
            }
        }
        number1 += 1;
        if number1 >= 10 {
            break 'loop1;
        }
    }
}
