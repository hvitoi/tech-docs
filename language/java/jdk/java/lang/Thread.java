class Main {
  public static void main(String[] args) {
    // Static methods
    ThreadNew.run();
    ThreadSleep.run();

    // Instance methods
    ThreadStart.run();
  }
}

class ThreadNew {
  static void run() {
    Thread thread = new Thread(() -> System.out.println("I will run in a new thread"));
  }
}

class ThreadSleep {
  static void run() {
    try {
      Thread.sleep(1000); // thread sleeps 1s
    } catch (InterruptedException e) {
    }
  }
}

class ThreadStart {
  static void run() {
    Thread thread = new Thread(() -> System.out.println("I will run in a new thread"));
    thread.start();
  }
}