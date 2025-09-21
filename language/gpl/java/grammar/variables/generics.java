import java.util.ArrayList;
import java.util.stream.Stream;

class Main {

  public static void main(String[] args) {

    /**
     * Generics on a constructor
     */
    var list = new ArrayList<String>();
    var stringBox = new Box<>("Hello"); // type is inferred from the content
    var intBox = new Box<>(123); // type is inferred from the content

    /**
     * Generics on a static method
     */
    var stream = Stream.<String>empty();
    Foo.<Integer>printArray(new Integer[] { 1, 2, 3 });
    Foo.printArray(new String[] { "a", "b", "c" });

  }
}

// T is a type parameter.
class Box<T> {
  private T content;

  public Box(T content) {
    this.content = content;
  }

  public T getContent() {
    return content;
  }

}

class Foo {
  public static <T> void printArray(T[] array) {
    for (T element : array) {
      System.out.println(element);
    }
  }
}
