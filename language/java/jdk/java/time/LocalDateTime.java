import java.time.LocalDate;
import java.time.LocalDateTime;
import java.time.ZoneOffset;
import java.time.format.DateTimeFormatter;

class Main {
  public static void main(String[] args) {

    // Static methods
    _now.run();
    _parse.run();

    // Instance methods
    _format.run();
    _toEpochSecond.run();
    _toLocalDate.run();

  }
}

class _now {
  static void run() {
    LocalDateTime time = LocalDateTime.now(); // current time
  }
}

class _parse {
  static void run() {
    String str = "24/05/2022 20:12";
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");

    LocalDateTime time = LocalDateTime.parse(str, formatter);
  }
}

class _format {
  static void run() {
    LocalDateTime time = LocalDateTime.now();
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");

    String str = time.format(formatter);
  }
}

class _toEpochSecond {
  static void run() {
    LocalDateTime time = LocalDateTime.now();
    long epochTime = time.toEpochSecond(ZoneOffset.UTC);
  }
}

class _toLocalDate {
  static void run() {
    LocalDateTime time = LocalDateTime.now();
    LocalDate date = time.toLocalDate();
  }
}
