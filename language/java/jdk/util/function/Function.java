import java.util.function.Function;

// One Input -> One Output

class Main {
  public static void main(String[] args) {

    // Static methods
    FunctionNew.run();

    // Instance methods
    FunctionApply.run();
    FunctionAndThen.run();

  }
}

class FunctionNew {
  static void run() {
    Function<String, Integer> fn = (word) -> word.length();
  }
}

class FunctionApply {
  static void run() {
    Function<String, Integer> fn = (word) -> word.length();
    Integer res = fn.apply("henrique"); // 8

  }
}

class FunctionAndThen {
  static void run() {
    Function<String, Integer> fn1 = x -> x.length();
    Function<Integer, Integer> fn2 = x -> x * 2;

    Function<String, Integer> compositeFn = fn1.andThen(fn2);
    Integer res = compositeFn.apply("henrique"); // 16

  }
}