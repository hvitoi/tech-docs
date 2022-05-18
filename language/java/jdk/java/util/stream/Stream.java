import java.util.Collection;
import java.util.Map;
import java.util.Optional;
import java.util.Set;
import java.util.function.BinaryOperator;
import java.util.function.Supplier;
import java.util.stream.Collectors;
import java.util.stream.Stream;

class Main {
  public static void main(String[] args) {

    FunctionSupplierGet.run();

    // Static methods
    StreamBuilder.run();
    StreamEmpty.run();
    StreamOf.run();
    StreamGenerate.run();
    StreamIterate.run();

    // Intermediate operations
    StreamFilter.run();
    StreamLimit.run();
    StreamMap.run();
    StreamSkip.run();
    StreamSorted.run();

    // Terminal operations
    StreamAnyMatch.run();
    StreamCount.run();
    StreamForEach.run();
    StreamFindFirst.run();
    StreamFindAny.run();
    StreamCollect.run();
    StreamReduce.run();
    StreamToArray.run();

  }
}

class FunctionSupplierGet {
  static Stream<String> run() {
    // a new stream is created when supplier is invoked
    Supplier<Stream<String>> streamSupplier = () -> Stream.of("henry", "albert", "john");
    return streamSupplier.get();
  }
}

class StreamBuilder {
  static Stream<String> run() {
    Stream<String> streamBuilder = Stream.<String>builder().add("henry").add("albert").add("john").build();
    return streamBuilder;
  }
}

class StreamEmpty {
  static void run() {
    Stream stream = Stream.empty();
  }
}

class StreamOf {
  static void run() {
    // Stream object can be used only once (Java 8 streams can't be reused)
    Stream stream = Stream.of("henry", "albert", "john");
    Stream<String> stream2 = Stream.of("henry", "albert", "john");
  }
}

class StreamGenerate {
  static void run() {
    Stream<String> streamGenerated = Stream.generate(() -> "element").limit(10); // 10 strings with the value “element”
  }
}

class StreamIterate {
  static void run() {
    Stream<Integer> streamIterated = Stream.iterate(40, n -> n + 2).limit(20);
  }
}

class StreamFilter {
  static void run() {
    Stream<String> stream = StreamBuilder.run();
    Stream<String> filtered = stream.filter(e -> e.length() >= 4); // find the String than has length > 4
    // Stream<String> filtered2 = stream.filter(e -> {
    // return e.length() >= 4;
    // });
  }
}

class StreamLimit {
  static void run() {
    Stream<String> stream = StreamBuilder.run();
    Stream<String> limited = stream.limit(3);
  }
}

class StreamMap {
  static void run() {
    Stream<String> stream = StreamBuilder.run();
    Stream<String> mapped = stream.map(e -> e.substring(0, 3));
  }
}

class StreamSkip {
  static void run() {
    Stream<String> stream = StreamBuilder.run();
    Stream<String> skipped = stream.skip(1); // discard the first n elements of the stream
  }
}

class StreamSorted {
  static void run() {
    Stream<String> stream = StreamBuilder.run();
    Stream<String> sorted = stream.sorted();
  }
}

class StreamAnyMatch {
  static void run() {
    Stream<String> stream = StreamBuilder.run();
    boolean anyMatch = stream.anyMatch(e -> e.equals("henry")); // true
  }
}

class StreamCount {
  static void run() {
    Stream<String> stream = StreamBuilder.run();
    Long count = stream.count();
  }
}

class StreamForEach {
  static void run() {
    Stream<String> stream = StreamBuilder.run();
    // stream.forEach(System.out::println);
    // stream.forEach((el) -> System.out.println(el));
  }
}

class StreamFindFirst {
  static void run() {
    Stream<String> stream = StreamBuilder.run();
    Optional<String> found = stream.filter(e -> e.equals("a")).findFirst();
    // .orElseThrow(() -> new RuntimeException());
  }
}

class StreamFindAny {
  static void run() {
    Stream<String> stream = StreamBuilder.run();
    Optional<String> found = stream.filter(e -> e.equals("a")).findAny();
  }
}

class StreamCollect {
  static void run() {

    Stream<String> stream1 = StreamBuilder.run();
    Stream<String> stream2 = StreamBuilder.run();
    Stream<String> stream3 = StreamBuilder.run();

    // From stream to List
    Collection list = stream1.collect(Collectors.toList());

    // From stream to Set
    Set set = stream2.collect(Collectors.toSet());

    // From stream to Map
    Map col = stream3.collect(Collectors.toMap(u1 -> u1.toString(), u1 -> u1.toString()));
  }
}

class StreamReduce {
  static void run() {
    BinaryOperator<Integer> fn = (sum, num) -> sum + num;
    Integer res = Stream.of(1, 2, 3, 4).reduce(0, fn); // 10
  }
}

class StreamToArray {
  static void run() {
    Stream<String> stream = StreamBuilder.run();
    Object[] arr = stream.toArray();
  }
}
