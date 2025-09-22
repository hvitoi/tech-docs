import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.ZoneOffset;
import java.time.format.DateTimeFormatter;

class Main {
  public static void main(String[] args) {
    // Static methods
    _now();
    _parse();

    // Instance methods
    _format();
    _toEpochSecond();
    _toLocalDate();
  }

  static void _now() {
    LocalDateTime time = LocalDateTime.now(); // current time
  }

  static void _parse() {
    String str = "24/05/2022 20:12";
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");

    LocalDateTime time = LocalDateTime.parse(str, formatter);
  }

  static void _format() {
    LocalDateTime time = LocalDateTime.now();
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");

    String str = time.format(formatter);
  }

  static void _toEpochSecond() {
    LocalDateTime time = LocalDateTime.now();
    long epochTime = time.toEpochSecond(ZoneOffset.UTC);
  }

  static void _toLocalDate() {
    LocalDateTime time = LocalDateTime.now();
    LocalDate date = time.toLocalDate();
  }
}
