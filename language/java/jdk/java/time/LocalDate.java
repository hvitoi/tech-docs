import java.time.LocalDateTime;
import java.time.LocalDate;
import java.time.ZoneOffset;
import java.time.format.DateTimeFormatter;

class Main {
  public static void main(String[] args) {

    // Static methods
    _now();

    // Instance methods
    _plusDays();

  }

  static void _now() {
    LocalDate now = LocalDate.now();
  }

  static void _plusDays() {
    LocalDate now = LocalDate.now();
    now.plusDays(1);
  }
}
