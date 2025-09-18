class Main {
  public static void main(String[] args) {
    // Immutable data carriers
    // Automatically generate equals(), hashCode(), toString()

    record User(String name, int age) {
    }
    var user = new User("Alice", 25);
  }
}
