class Main {
  public static void main(String[] args) {
    do_something("Henry", "A", "B");
  }

  static void do_something(String name, String... surnames) {
    // additional params are passed as an array
    for (var surname : surnames) {
      System.out.println(surname);
    }
  }
}
