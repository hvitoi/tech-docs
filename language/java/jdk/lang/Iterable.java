import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Consumer;

class Main {
  public static void main(String[] args) {
    IterableForEach.run();
  }
}

class IterableForEach {
  // inherited from java.lang.Iterable
  static void run() {
    Iterable<String> stringData = Arrays.asList("john", "tom", "jane");

    Consumer<String> consumer1 = (el) -> System.out.println(el);
    Consumer<String> consumer2 = System.out::println;
    Consumer<String> consumer3 = new MyConsumerClass();

    stringData.forEach(consumer1);
    stringData.forEach(consumer2);
    stringData.forEach(consumer3);

  }
}

class MyConsumerClass implements Consumer<String> {

  @Override
  public void accept(String str) {
    System.out.println(str);
  }

}