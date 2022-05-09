import java.util.Comparator;

class Main {
  public static void main(String[] args) {
    AnonymousClass.run();

  }
}

class AnonymousClass {
  static void run() {

    // Anonymous classes are inner classes with no name.
    // Declare and instantiate anonymous classes in a single expression
    Object isEqual = new Comparator<String>() {
      @Override
      public int compare(String s1, String s2) {
        return s1.compareTo(s2);
      }
    };

    System.out.println(isEqual);
  }
}