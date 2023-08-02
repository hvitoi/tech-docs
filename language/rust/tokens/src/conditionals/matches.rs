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
    let foo = match x {
        'a' => 'z',

        // else case
        _ => 'x',
    };
}
