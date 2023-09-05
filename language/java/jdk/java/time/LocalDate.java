import java.time.LocalDateTime;
import java.time.LocalDate;
import java.time.ZoneOffset;
import java.time.format.DateTimeFormatter;

class Main {
  public static void main(String[] args) {

    // Static methods
    _now.run();

    // Instance methods
    _plusDays.run();

  }
}

class _now {
  static void run() {
    LocalDate now = LocalDate.now();
  }
}

class _plusDays {
  static void run() {
    LocalDate now = LocalDate.now();
    now.plusDays(1);
  }
}