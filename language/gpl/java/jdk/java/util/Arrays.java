import java.util.Arrays;

class Main {
  public static void main(String[] args) {
    // Static methods
    _asList();
    _sort();
    _stream();
  }

  static void _asList() {
    var list1 = Arrays.asList(new int[] { 1, 2, 3 });
    var list2 = Arrays.asList(1, 2, 3);
    var list3 = Arrays.asList("alpha", "beta", "gamma");
  }

  static void _sort() {
    int[] arr = { 3, 1, 2 };
    Arrays.sort(arr);
  }

  static void _stream() {
    // Convert an array into a Stream
    var arr = new String[] { "john", "tom", "jane" };
    var stream = Arrays.stream(arr);
  }
}
