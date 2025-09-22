// Abstract Class

import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

class Main {
  public static void main(String[] args) {
    _new();

    // Instance methods
    _getTime();
  }

  static void _new() {
    Calendar calendar = new GregorianCalendar();
  }

  static void _getTime() {
    var calendar = new GregorianCalendar();
    Date date = calendar.getTime();
  }
}
