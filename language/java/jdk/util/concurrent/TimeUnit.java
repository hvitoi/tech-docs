import java.util.concurrent.TimeUnit;

class Main {
  public static void main(String[] args) {
    TimeUnitSleep.run();
  }
}

class TimeUnitSleep {
  static void run() {
    try {
      TimeUnit.SECONDS.sleep(5);
    } catch (InterruptedException e) {
      e.printStackTrace();
    }
  }
}