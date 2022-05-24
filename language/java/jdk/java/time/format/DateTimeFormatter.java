import java.time.format.DateTimeFormatter;

class Main {
  public static void main(String[] args) {

    // Static methods
    DateTimeFormatterOfPattern.run();

  }
}

class DateTimeFormatterOfPattern {
  static void run() {
    // Creates a formatter using a specific pattern.
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");

  }
}