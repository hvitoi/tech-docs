import java.util.Scanner;

class Main {
  public static void main(String[] args) {
    _new();

    // Instance methods
    _nextLine();
  }

  static void _new() {
    Scanner scanner = new Scanner(System.in);
  }

  static void _nextLine() {
    // Read from stdin
    try (var scanner = new Scanner(System.in)) {
      String input = scanner.nextLine();
      System.out.println("You typed: " + input);
    }
  }
}
