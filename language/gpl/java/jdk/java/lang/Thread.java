class Main {
  public static void main(String[] args) {
    // Static methods
    _new();
    _sleep();
    _currentThread();

    // Instance methods
    _start();
    _getName();
  }

  static void _new() {
    Runnable myFunction = () -> System.out.println("I will run in a new thread");
    Thread thread = new Thread(myFunction);
  }

  static void _sleep() {
    try {
      // sleeps the current thread (1s)
      Thread.sleep(1000);
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
  }

  static void _currentThread() {
    // get the thread object of the current thread
    Thread thread = Thread.currentThread();
  }

  static void _start() {
    var thread = new Thread(() -> System.out.println("I will run in a new thread"));
    thread.start();
  }

  static void _getName() {
    var thread = new Thread(() -> System.out.println(""));
    thread.getName();
  }
}
