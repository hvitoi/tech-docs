class Main {
  public static void main(String[] args) {

    // Static methods
    _new.run();
    _printStackTrace.run();
  }
}

class _new {
  static void run() {
    Exception e = new Exception();
  }
}

class _printStackTrace {
  static void run() {
    Exception e = new Exception();
    e.printStackTrace();
  }
}
