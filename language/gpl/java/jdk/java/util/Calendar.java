import java.util.Calendar;
import java.util.Date;
import java.util.GregorianCalendar;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    _getTime();
  }

  static Calendar _new() {
    Calendar calendar = new GregorianCalendar();
    return calendar;
  }

  static void _getTime() {
    Calendar calendar = _new();
    Date date = calendar.getTime();
  }
}
