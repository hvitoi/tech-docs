/*
 * Thread class
 */

class Main {
  public static void main(String[] args) {
    /*
     * Static
     */
    _new.run();
    _sleep.run();
    _currentThread.run();

    /*
     * Instance
     */
    _start.run();
    _getName.run();
  }
}

class _new {
  static void run() {
    new Thread(() -> System.out.println("I will run in a new thread"));
  }
}

class _sleep {
  static void run() {
    try {
      // sleeps the current thread (1s)
      Thread.sleep(1000);
    } catch (InterruptedException e) {
    }
  }
}

class _currentThread {
  static void run() {
    // get the thread object of the current thread
    Thread.currentThread();
  }
}

class _start {
  static void run() {
    var thread = new Thread(() -> System.out.println("I will run in a new thread"));
    thread.start();
  }
}

class _getName {
  static void run() {
    var thread = new Thread(() -> System.out.println(""));
    thread.getName();
  }
}
