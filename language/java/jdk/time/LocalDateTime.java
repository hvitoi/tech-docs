import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;

class Main {
  public static void main(String[] args) {

    // Static methods
    LocalDateTimeNow.run();

    // Instance methods
    LocalDateTimeFormat.run();

  }
}

class LocalDateTimeNow {
  static void run() {
    LocalDateTime time = LocalDateTime.now(); // current time
  }
}

class LocalDateTimeFormat {
  static void run() {
    LocalDateTime time = LocalDateTime.now();
    time.format(DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm"));
  }
}