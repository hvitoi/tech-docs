import java.time.LocalDateTime;
import java.time.ZoneOffset;
import java.time.format.DateTimeFormatter;

class Main {
  public static void main(String[] args) {

    // Static methods
    LocalDateTimeNow.run();
    LocalDateTimeParse.run();

    // Instance methods
    LocalDateTimeFormat.run();
    LocalDateTimeToEpochSecond.run();

  }
}

class LocalDateTimeNow {
  static void run() {
    LocalDateTime time = LocalDateTime.now(); // current time
  }
}

class LocalDateTimeParse {
  static void run() {
    String str = "24/05/2022 20:12";
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

class LocalDateTimeToEpochSecond {
  static void run() {
    LocalDateTime time = LocalDateTime.now();
    long epochTime = time.toEpochSecond(ZoneOffset.UTC);
  }
}
