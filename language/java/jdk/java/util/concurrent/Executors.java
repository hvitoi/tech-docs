/*
 * Executors class
 */

import java.util.concurrent.Executors;

class Main {
  public static void main(String[] args) {
    /**
     * Static
     */
    _newCachedThreadPool.run();
    _newFixedThreadPool.run();
    _newScheduledThreadPool.run();
  }
}

class _newCachedThreadPool {
  static void run() {
    // This is used for light tasks that can be idle (e.g., http requests)
    Executors.newCachedThreadPool();

  }
}

class _newFixedThreadPool {
  static void run() {
    // If the task is a CPU intensive operations, there is not need to set the
    // number of threads higher than the availableProcessors. Because if all the
    // cores (physical threads) are busy, then the remaining virtual threads would
    // be pending a free slot

    // If the tasks is idle most of the time (e.g., http requests waiting for an
    // response), then you need to set a high number of virtual threads. Because
    // while a thread is waiting, the CPU core is is borrowed to another thread. Too
    // many thread will also increase the memory consumption

    // If a thread terminates due to a failure in the task, then a new thread with
    // the task is created to replace it
    int coreCount = Runtime.getRuntime().availableProcessors();
    Executors.newFixedThreadPool(coreCount);
  }
}

class _newScheduledThreadPool {
  static void run() {
    Executors.newScheduledThreadPool(1);
  }
}
