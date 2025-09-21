class Main {
  public static void main(String[] args) {
    int num;

    num = 1 + 2;
    num = 4 * 10;
    num = 20 / 5;
    num = 4 % 3;

    num = 0;
    num++;
    num--;
    num += 2;
    num -= 2;
    num *= 2;
    num /= 2;

    // Prefix
    num = 10;
    System.out.println(num--); // Outputs 10 (print and then decrement)
    System.out.println(num); // Outputs 9

    // Postfix
    num = 10;
    System.out.println(--num); // Outputs 10 (decrement and then print)
    System.out.println(num); // Outputs 10

  }
}
