fn main() {
    let a = 6; // 00000110
    let b = 12; // 00001100

    // AND
    println!("{:08b}", a & b); // 00000100 (4)

    // OR
    println!("{:08b}", a | b); // 00001110 (14)

    // XOR
    println!("{:08b}", a ^ b); // 00001010 (10)

    // SHIFT LEFT
    println!("{:08b}", a << 1); // 00001100 (12)

    // SHIFT RIGHT
    println!("{:08b}", a >> 1); // 00000011 (3)
}
