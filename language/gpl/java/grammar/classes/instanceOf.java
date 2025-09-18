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
  }
}
