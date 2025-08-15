import java.util.function.Predicate;

// One Input -> Boolean
class Main {
  public static void main(String[] args) {
    // Static methods
    PredicateNew.run();
  }
}

class PredicateNew {
  static void run() {
    Predicate<String> startsWithS = str -> str.startsWith("S"); // true or false
  }
}
