import java.util.Optional;
import java.util.function.BinaryOperator;
import java.util.function.Supplier;
import java.util.stream.Collectors;
import java.util.stream.Stream;

// Stream API has been introduced in Java 8
// Streams can't be reused

class Main {
  public static void main(String[] args) {
    // Static methods
    _of();
    _empty();
    _generate();
    _iterate();
    _builder();

    // Intermediate operations (return another stream)
    _map();
    _filter();
    _sorted();
    _skip();
    _limit();

    // Terminal operations (return a value)
    _forEach();
    _reduce();
    _count();
    _anyMatch();
    _findFirst();
    _findAny();
    _collect();
    _toArray();
  }

  static void _of() {
    var stream = Stream.of("a", "b", "c");

    Supplier<Stream<String>> streamSupplier = () -> Stream.of("a", "b", "c");
    var stream2 = streamSupplier.get();
  }

  static void _empty() {
    var stream = Stream.<String>empty();
  }

  static void _generate() {
    // 10 strings with the value "foo"
    var stream = Stream
        .generate(() -> "foo")
        .limit(10);
  }

  static void _iterate() {
    // [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    var stream = Stream
        .iterate(0, x -> x + 1)
        .limit(10);
  }

  static void _builder() {
    var streamBuilder = Stream.<String>builder();
    var stream = streamBuilder
        .add("henry")
        .add("john")
        .build();
  }

  static void _map() {
    var stream = Stream.of("a", "b", "c");
    stream.map(e -> e.toUpperCase());
  }

  static void _filter() {
    var stream = Stream.of(1, 2, 3, 4);
    stream.filter(e -> e % 2 == 0);
  }

  static void _sorted() {
    var stream = Stream.of("a", "b", "c");
    stream.sorted();
  }

  static void _skip() {
    // discard the first n elements of the stream
    var stream = Stream.of("a", "b", "c");
    stream.skip(1);
  }

  static void _limit() {
    var stream = Stream.of("a", "b", "c");
    stream.limit(2);
  }

  static void _forEach() {
    // returns nothing
    var stream = Stream.of("a", "b", "c");
    // stream.forEach(System.out::println);
  }

  static void _reduce() {
    var stream = Stream.of(1, 2, 3, 4, 5);

    BinaryOperator<Integer> reducerFn = (acc, num) -> acc + num;
    stream.reduce(0, reducerFn);
  }

  static void _count() {
    var stream = Stream.of("a", "b", "c");
    stream.count(); // 3
  }

  static void _anyMatch() {
    var stream = Stream.of("a", "b", "c");
    stream.anyMatch(e -> e.equals("b")); // true
  }

  static void _findFirst() {
    // Get the first element of a stream
    var stream = Stream.of("a", "b", "c");
    Optional<String> found = stream
        .findFirst();
    // .orElseThrow(() -> new RuntimeException());
  }

  static void _findAny() {
    // Gets an any element of the stream
    // The element is usually the first, but it's not guaranteed! (like findFirst)
    var stream = Stream.of("a", "b", "c");
    Optional<String> found = stream
        .findAny();
  }

  static void _collect() {
    var stream1 = Stream.of("a", "b", "c");
    var stream2 = Stream.of("a", "b", "c");
    var stream3 = Stream.of("a", "b", "c");

    stream1.collect(Collectors.toList());
    stream2.collect(Collectors.toSet());
    stream3.collect(Collectors.toMap(el -> el, el -> el.repeat(3)));
  }

  static void _toArray() {
    var stream = Stream.of("a", "b", "c");
    Object[] arr = stream.toArray();
  }

}
