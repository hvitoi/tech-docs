# Bit Shifting

- Manipulation of bits to produce the results desired (e.g., addition, subtraction, multiplication, etc)

## AND

- **&** operator
- The `and` operation shows what are the `carries` (vai um)
- The in order for the carries to be properly added, they need to be `shifted to the left`

```rust
let a = 6; // 0000 0110
let b = 12; // 000 01100

println!("{:08b}", a & b); // 0000 0100 (4)
```

## OR

- **|** operator

```rust
let a = 6; // 0000 0110
let b = 12; // 000 01100

println!("{:08b}", a | b); // 0000 1110 (14)
```

## XOR

- **^** operator
- The `xor` operator "simulates" a sum by showing what are the sum of the elements ignoring the carries

```rust
let a = 6; // 0000 0110
let b = 12; // 000 01100

println!("{:08b}", a ^ b); // 0000 1010 (10)
```

## NOT

- **~** operator

```rust
let a = 6; // 0000 0110

println!("{:08b}", a ~ b);
```

## Shift Left

- **<<** operator
- Multiplies by 2

```rust
let a = 6; // 0000 0110

println!("{:08b}", a << 1); // 0000 1100 (12)
```

## Shift Right

- **>>** operator
- Divides by 2

```rust
let a = 6; // 0000 0110

println!("{:08b}", a >> 1); // 0000 0011 (3)
```

## Carry

- `Generate a carry`: no carry is receiving, but a carry is created
- `Propagate a carry`: a carry is received and a carry is created

## Applications of bitwise

- **Sum**
    1. Find the carries `&`
    1. Shift the carries to the left `<<`
    1. Add the numbers without the carries `^`
    1. Add the sum (without carries) + the left shifted carries `&`

```python
carry_lookahead = ((a & b) << 1)

full_adder = (a ^ b) + carry_lookahead
```
