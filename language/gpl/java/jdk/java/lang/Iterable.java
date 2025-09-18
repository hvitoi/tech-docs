import java.util.List;
import java.util.function.Consumer;

class Main {
  public static void main(String[] args) {
    _forEach();
  }

  static void _forEach() {
    var data = List.of("a", "b", "c");

    Consumer<String> consumer1 = (el) -> System.out.println(el);
    Consumer<String> consumer2 = System.out::println;

    data.forEach(consumer1);
    data.forEach(consumer2);
  }
}
