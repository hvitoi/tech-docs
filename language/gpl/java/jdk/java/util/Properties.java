import java.util.Map;
import java.util.Properties;

class Main {
  public static void main(String[] args) {
    _new();

    // Instance methods
    _getProperty(); // -> String
    _setProperty(); // -> Void
    _putAll(); // -> Void
  }

  static void _new() {
    Properties props = new Properties();
  }

  static void _getProperty() {
    var props = new Properties();
    var prop = props.getProperty("a");
  }

  static void _setProperty() {
    var props = new Properties();
    props.setProperty("a", "alpha");
  }

  static void _putAll() {
    var props = new Properties();
    // set all key-value pairs contained inside of a map
    props.putAll(Map.of("a", 1, "b", 2));
  }

}
