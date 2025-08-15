/*
 * Thread class
 */

class Main {
  public static void main(String[] args) {
    /*
     * Static
     */
    _new();
    _sleep();
    _currentThread();

    /*
     * Instance
     */
    _start();
    _getName();
  }

  static void _new() {
    new Thread(() -> System.out.println("I will run in a new thread"));
  }

  static void _sleep() {
    try {
      // sleeps the current thread (1s)
      Thread.sleep(1000);
    } catch (InterruptedException e) {
    }
  }

  static void _currentThread() {
    // get the thread object of the current thread
    Thread.currentThread();
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
