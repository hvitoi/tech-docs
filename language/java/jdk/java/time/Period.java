import java.time.Period;
import java.time.LocalDate;

class Main {
  public static void main(String[] args) {

    // Static methods
    PeriodNew.run();

    // Instance methods
    PeriodGetYears.run();
  }
}

class PeriodNew {
  static void run() {
    Period period = Period.between(LocalDate.now(), LocalDate.now());
    System.out.println(period.getYears());
  }
}

class PeriodGetYears {
  static void run() {
    Period period = Period.between(LocalDate.now(), LocalDate.now());
    int years = period.getYears();
  }
}
