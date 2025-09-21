class Main {

  // Available as of Java 21 (standard)

  public static void main(String[] args) {

    // Switch Expression (Java 14)
    var day = 2;
    String dayOfTheWeek = switch (day) {
      case 1 -> "Monday";
      case 2 -> "Tuesday";
      default -> "Unknown";
    };
    System.out.println(dayOfTheWeek);

    // Switch Expression with Pattern Matching (Java 21)
    // each "case" checks the instance type and casts if valid
    Object obj = "Henry";
    var text = switch (obj) {
      case String s -> "String of length " + s.length();
      case Integer i -> "Integer with value " + i;
      case Double d -> "Double with value " + d;
      case null -> "Null value";
      default -> "Something else: " + obj;
    };
    System.out.println(text);

  }
}
