import java.time.Clock;
import java.time.Instant;
import java.time.ZoneId;

class Main {
  public static void main(String[] args) {

    // Static methods
    _systemUTC();
    _systemDefaultZone();
    _system();

  }

  static void _systemUTC() {
    // UTC clock
    Clock clock = Clock.systemUTC();
    System.out.println(clock); // SystemClock[Z]
  }

  static void _systemDefaultZone() {
    // The clock of the timezone in which this code is running
    Clock clock = Clock.systemDefaultZone();
    System.out.println(clock); // SystemClock[America/Sao_Paulo]
  }

  static void _system() {
    // The clock of an arbitrary timezone
    ZoneId zone = ZoneId.of("Asia/Tokyo");
    Clock clock = Clock.system(zone);
    System.out.println(clock);
  }

}
