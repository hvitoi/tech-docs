import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

public class Main {
  public static void main(String[] args) {
    // Static methods
    CalendarNew.run();

    // Instance methods
    CalendarGetTime.run();

  }
}

class CalendarNew {
  static Calendar run() {
    Calendar calendar = new GregorianCalendar();
    return calendar;
  }
}

class CalendarGetTime {
  static void run() {
    Calendar calendar = CalendarNew.run();
    Date date = calendar.getTime();
  }
}