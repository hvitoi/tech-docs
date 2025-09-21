class Main {
  public static void main(String[] args) {
    Object obj = "hello";

    if (obj instanceof String) { // check
      var s = (String) obj; // cast manually
      System.out.println(s.toUpperCase());
    }

    // Pattern Matching (Java 16)
    if (obj instanceof String s) { // check and cast
      System.out.println("String length: " + s.length());
    } else if (obj instanceof Integer i) {
      System.out.println("Integer value: " + i);
    }

    // Switch Expression with Pattern Matching (Java 21)
    // each "case" checks the instance type and casts if valid
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
