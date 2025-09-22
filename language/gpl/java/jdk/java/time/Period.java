import java.time.LocalDate;
import java.time.Period;

class Main {
  public static void main(String[] args) {
    // Static methods
    _between();

    // Instance methods
    _getYears();
  }

  static void _between() {
    Period period = Period.between(LocalDate.now(), LocalDate.now());
    System.out.println(period.getYears());
  }

  static void _getYears() {
    Period period = Period.between(LocalDate.now(), LocalDate.now());
    int years = period.getYears();
  }
}
