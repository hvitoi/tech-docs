class Main {
  public static void main(String[] args) {
    // Static Methods
    StringBuilderNew.run();

    // Instance methods
    StringBuilderAppend.run();
    StringBuilderToString.run();
  }
}

class StringBuilderNew {
  static void run() {
    StringBuilder builder = new StringBuilder("hey");
  }
}

class StringBuilderAppend {
  static void run() {
    StringBuilder builder = new StringBuilder("hey");
    builder.append(" there!");
    System.out.println(builder.toString());
  }
}

class StringBuilderToString {
  static void run() {
    StringBuilder builder = new StringBuilder("hey");
    builder.append(" there!");
    System.out.println(builder.toString());
  }
}