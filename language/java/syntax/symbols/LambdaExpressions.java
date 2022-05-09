class Main {
  public static void main(String[] args) {
    LambdaExpressions.run();

  }
}

class LambdaExpressions {
  static void run() {

    Object res = () -> {
      return 9;
    };

    Object res2 = () -> 9;

  }
}