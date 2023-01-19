/*
 * ScheduledExecutorService class
 */

import java.util.concurrent.ExecutorService;
import java.util.concurrent.Executors;

class Main {
  public static void main(String[] args) {
    var executorService = Init.run();

    /**
     * Instance
     */
    _submit.run(executorService);
  }

}

class Init {
  static ExecutorService run() {
    return Executors.newCachedThreadPool();
  }
}

class _submit {
  static void run(ExecutorService executorService) {

  }
}
