import java.text.SimpleDateFormat;
import java.util.Date;

class Main {
  public static void main(String[] args) {
    _new();
  }

  static void _new() {
    Date date = new Date();
    SimpleDateFormat formatter = new SimpleDateFormat("dd-MM-yyyy HH:mm:ss");
    System.out.println(formatter.format(date));
  }

}
