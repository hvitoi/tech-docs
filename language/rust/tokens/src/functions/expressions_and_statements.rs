fn main() {
    let x = 4;

    let y = {
        let x_squared = x * x;
        let x_cubed = x * x * x;

        // x + x_squared + x_cubed; // if a semicolon if placed, the return value is suppressed and the return is an empty unit
        x + x_squared + x_cubed // The evaluation is an expression! (doesn't change state)
    }; // The variable assignment is a statement! (does changes state)

    println!("{}", y);

    // Useless but works
    let a = {
        let a = 2;
        a
    };
}
