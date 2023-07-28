
int main() {

  // bit level programming

  // & AND
  // | OR
  // ^ XOR
  // << left shift (shift n bits to the left) - Truncates a bit and adds a 0
  // >> right shift (shift n bits to the right) - Truncates a bit and adds a 0

  int x = 6;  // 00000110 -> 6
  int y = 12; // 00001100 -> 12
  int z = 0;  // 00000000 -> 0

  // compare each bit
  z = x & y;  // 00000100 -> 4
  z = x | y;  // 00001110 -> 14
  z = x ^ y;  // 00001010 -> 10
  z = x << 1; // 00001100 -> 12 (Shifting to the left doubles it!)
  z = x >> 1; // 00000011 -> 3  (Shifting to the right halves it!)

  return 0;
}
