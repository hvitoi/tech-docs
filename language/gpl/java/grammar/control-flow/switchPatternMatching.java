class Main {

  // Available as of Java 21 (standard)

  public static void main(String[] args) {
    Object obj = "Henry";

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
