import java.util.Optional;
import java.util.function.BinaryOperator;
import java.util.function.Supplier;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class Main {
  public static void main(String[] args) {
    // Static methods
    _builder();
    _empty();
    _of();
    _generate();
    _iterate();

    // Intermediate operations
    _filter();
    _limit();
    _map();
    _skip();
    _sorted();

    // Terminal operations
    _anyMatch();
    _count();
    _forEach();
    _findFirst();
    _findAny();
    _collect();
    _reduce();
    _toArray();
  }

  static Stream<String> _builder() {
    var streamBuilder = Stream.<String>builder()
        .add("henry")
        .add("albert")
        .add("john")
        .build();
    return streamBuilder;
  }

  static void _empty() {
    var stream = Stream.empty();
  }

  static void _of() {
    // Stream object can be used only once (Java 8 streams can't be reused)
    var stream = Stream.of("henry", "albert", "john");
    Stream<String> stream2 = Stream.of("henry", "albert", "john");

    Supplier<Stream<String>> streamSupplier = () -> Stream.of("henry", "albert", "john");
    streamSupplier.get();
  }

  static void _generate() {
    // 10 strings with the value “element”
    var streamGenerated = Stream
        .generate(() -> "element")
        .limit(10);
  }

  static void _iterate() {
    var streamIterated = Stream
        .iterate(40, n -> n + 2)
        .limit(20);
  }

  static void _filter() {
    Stream<String> stream = _builder();
    Stream<String> filtered = stream.filter(e -> e.length() >= 4); // find the String than has length > 4
    // Stream<String> filtered2 = stream.filter(e -> {
    // return e.length() >= 4;
    // });
  }

  static void _limit() {
    Stream<String> stream = _builder();
    Stream<String> limited = stream.limit(3);
  }

  static void _map() {
    Stream<String> stream = _builder();
    Stream<String> mapped = stream.map(e -> e.substring(0, 3));
  }

  static void _skip() {
    Stream<String> stream = _builder();
    Stream<String> skipped = stream.skip(1); // discard the first n elements of the stream
  }

  static void _sorted() {
    Stream<String> stream = _builder();
    Stream<String> sorted = stream.sorted();
  }

  static void _anyMatch() {
    Stream<String> stream = _builder();
    boolean anyMatch = stream.anyMatch(e -> e.equals("henry")); // true
  }

  static void _count() {
    Stream<String> stream = _builder();
    Long count = stream.count();
  }

  static void _forEach() {
    Stream<String> stream = _builder();
    stream.forEach(System.out::println);
    // stream.forEach((el) -> System.out.println(el));
  }

  static void _findFirst() {
    Stream<String> stream = _builder();
    Optional<String> found = stream
        .filter(e -> e.equals("a"))
        .findFirst();
    // .orElseThrow(() -> new RuntimeException());
  }

  static void _findAny() {
    Stream<String> stream = _builder();
    Optional<String> found = stream
        .filter(e -> e.equals("a"))
        .findAny();
  }

  static void _collect() {
    Stream<String> stream1 = _builder();
    Stream<String> stream2 = _builder();
    Stream<String> stream3 = _builder();

    // From stream to List
    var list = stream1.collect(Collectors.toList());

    // From stream to Set
    var set = stream2.collect(Collectors.toSet());

    // From stream to Map
    var col = stream3.collect(Collectors.toMap(u1 -> u1.toString(), u1 -> u1.toString()));
  }

  static void _reduce() {
    BinaryOperator<Integer> fn = (sum, num) -> sum + num;
    Integer res = Stream.of(1, 2, 3, 4)
        .reduce(0, fn); // 10
  }

  static void _toArray() {
    Stream<String> stream = _builder();
    Object[] arr = stream.toArray();
  }

}
