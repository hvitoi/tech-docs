import java.util.Arrays;
import java.util.List;
import java.util.stream.Stream;

class Main {
  public static void main(String[] args) {

    // Instance methods
    _sort();
    _asList();
    _stream();

  }

  static void _sort() {
    int[] arr = { 43, 15, 64, 22, 89 };
    Arrays.sort(arr);
  }

  static void _asList() {
    // Convert an array into a List
    List list1 = Arrays.asList(new int[] { 43, 15, 64, 22, 89 });
    List list2 = Arrays.asList(0, 1, 2, 3);
    List list3 = Arrays.asList("john", "tom", "jane");
  }

  static void _stream() {
    String[] arr = { "john", "tom", "jane" };

    // Convert an array into a List
    Stream stream = Arrays.stream(arr);
  }
}
