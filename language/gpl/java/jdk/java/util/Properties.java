import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Map;
import java.util.Properties;

class Main {
  public static void main(String[] args) {
    /**
     * Static
     */
    _new();

    /**
     * Instance
     */
    getProperty();
    putAll();
    setProperty();

  }

  static void _new() {
    Properties props = new Properties();
  }

  static void getProperty() {
    Properties props = new Properties();

    props.getProperty("a");
  }

  static void putAll() {
    Properties props = new Properties();

    // set all key-value pairs contained inside of a map
    props.putAll(Map.of("a", 1));
  }

  static void setProperty() {
    Properties props = new Properties();

    props.setProperty("a", "alpha");
  }
}
