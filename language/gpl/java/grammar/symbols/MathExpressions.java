class Main {
  public static void main(String[] args) {
    int num;

    num = 1 + 2;
    System.out.println("1 + 2 = " + num); // 3

    num = 4 * 10;
    System.out.println("4 * 10 = " + num); // 40

    num = 20 / 5;
    System.out.println("20 / 5 = " + num); // 4

    num = 4 % 3; // the remainder of (4 / 3)
    System.out.println("4 % 3 = " + num); // 1

    num = 0;
    num++;
    System.out.println("0 + 1 = " + num); // 1

    num = 0;
    num--;
    System.out.println("0 - 1 = " + num); // -1

    num = 0;
    num += 2;
    System.out.println("0 + 2 = " + num); // 2

    num = 0;
    num -= 2;
    System.out.println("0 - 2 = " + num); // - 2

    num = 10;
    num *= 2;
    System.out.println("10 * 2 = " + num); // 20

    num = 10;
    num /= 2;
    System.out.println("10 / 2 = " + num); //

    // Prefix
    num = 3;
    System.out.println(num--); // Outputs 3 (print and then decrement)
    System.out.println(num); // Outputs 2

    // Postfix
    num = 3;
    System.out.println(--num); // Outputs 2 (decrement and then print)
    System.out.println(num); // Outputs 2

  }
}
