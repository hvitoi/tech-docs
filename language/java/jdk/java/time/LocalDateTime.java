import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

class Main {
  public static void main(String[] args) {

    // Static methods
    LocalDateTimeNow.run();
    LocalDateTimeParse.run();

    // Instance methods
    LocalDateTimeFormat.run();

  }
}

class LocalDateTimeNow {
  static void run() {
    LocalDateTime time = LocalDateTime.now(); // current time
  }
}

class LocalDateTimeParse {
  static void run() {
    String str = "2022-05-24T20:12:36.622533";
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");

    LocalDateTime time = LocalDateTime.parse(str, formatter);
  }
}

class LocalDateTimeFormat {
  static void run() {
    LocalDateTime time = LocalDateTime.now();
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");

    String str = time.format(formatter);
  }
}