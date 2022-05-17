import java.text.SimpleDateFormat;
import java.util.Date;

public class Main {
  public static void main(String[] args) {
    // Static methods
    DateNew.run();

    // Instance methods
    DateGetTime.run();

  }
}

class DateNew {
  static void run() {
    new Date(); // Current date
    new Date(System.currentTimeMillis()); // Date from a unix epoch duration

    // format
    SimpleDateFormat formatter = new SimpleDateFormat("dd-MM-yyyy HH:mm:ss");
    System.out.println(formatter.format(new Date()));

  }
}

class DateGetTime {
  static void run() {
    Date date = new Date();

    Long time = date.getTime();

  }
}