import java.util.ArrayList;
import java.util.Comparator;
import java.util.List;

// Anonymous classes is a class without a name that is declared and instantiated out of an interface (or another class)
// Anonymous classes syntax work like an expression, not a declaration
// Anonymous classes are rare these these with the advent of lambdas

class Main {
  public static void main(String[] args) {

    // Anonymous class out of the Comparator interface
    Comparator<String> myComparator = new Comparator<String>() {
      @Override
      public int compare(String a, String b) {
        return a.compareTo(b);
      }
    };
    var list = new ArrayList<>(List.of("Charlie", "Alice", "Bob"));
    list.sort(myComparator);

    // Anonymous class out of the Runnable interface
    Runnable myRunnable = new Runnable() {
      @Override
      public void run() {
        System.out.println("Hello, World!");
      }
    };
    myRunnable.run();

  }
}
