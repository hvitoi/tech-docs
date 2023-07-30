fn main() {
    // decimal (10), hexadecimal (16), octal (8), binary (2)
    let a = 1_024 + 0xff + 0o77 + 0b1111_1111; // 1024 + 255 + 63 + 255
    print!("{}", a)
}
