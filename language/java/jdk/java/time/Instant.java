import java.time.Clock;
import java.time.Instant;
import java.time.ZoneId;

class Main {
  public static void main(String[] args) {

    // Static methods
    _now();

  }

  static void _now() {
    // UTC clock
    Instant inst = Instant.now();
    System.out.println(inst);
  }

}
