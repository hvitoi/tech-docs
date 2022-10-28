import java.time.Period;
import java.time.LocalDate;

class Main {
  public static void main(String[] args) {

    // Static methods
    Perioda.run();

  }
}

class Perioda {
  static void run() {
    // 5 seconds
    Period period = Period.between(LocalDate.now(), LocalDate.now());
    System.out.println(period.getYears());
  }
}
