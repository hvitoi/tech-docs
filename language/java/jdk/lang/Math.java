class Main {
  public static void main(String[] args) {

    /**
     * Static
     */
    MathAbs.run();
    MathRandom.run();

  }
}

class MathAbs {
  static void run() {
    int absolute = Math.abs(-1);
  }
}

class MathRandom {
  static void run() {
    double rand = Math.random(); // [0,1)
  }
}
