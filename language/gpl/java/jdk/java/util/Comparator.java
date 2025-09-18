import java.util.Comparator;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();
    _comparing();
  }

  static void _new() {
    var comparator1 = new PersonComparator(); // old way of creating comparators
    var comparator2 = (a, b) -> Integer.compare(a, b); // new syntax

  }

  static void _comparing() {
    // Comparator.comparing();
  }
}

class PersonComparator implements Comparator<Integer> {

  @Override
  public int compare(Integer a, Integer b) {
    return Integer.compare(a, b); // 0: equal, -1: smaller, +1: bigger
  }

}
