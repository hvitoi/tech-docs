import java.util.ArrayList;
import java.util.SequencedCollection;
import java.util.List;

class Main {
  public static void main(String[] args) {

    // Static methods
    _new();

    // Instance methods
    _reversed();

    // + Iterable methods
  }

  static void _new() {
    SequencedCollection<String> items = new ArrayList<>(List.of("a", "b", "c"));
  }

  static void _reversed() {
    SequencedCollection<String> items = new ArrayList<>(List.of("a", "b", "c"));
    items.reversed();
  }

}
