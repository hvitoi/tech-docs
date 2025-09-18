import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    getTime();

  }

  static Calendar _new() {
    Calendar calendar = new GregorianCalendar();
    return calendar;
  }

  static void getTime() {
    Calendar calendar = CalendarNew.run();
    Date date = calendar.getTime();
  }
}
