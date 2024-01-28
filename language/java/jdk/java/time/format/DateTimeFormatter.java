import java.time.format.DateTimeFormatter;

class Main {
  public static void main(String[] args) {

    // Static methods
    _ofPattern();

  }

  static void _ofPattern() {
    // Creates a formatter using a specific pattern.
    DateTimeFormatter formatter = DateTimeFormatter.ofPattern("dd/MM/yyyy HH:mm");

  }
}
