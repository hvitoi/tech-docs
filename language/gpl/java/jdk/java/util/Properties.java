import java.util.Map;
import java.util.Properties;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    _getProperty();
    _putAll();
    _setProperty();
  }

  static void _new() {
    Properties props = new Properties();
  }

  static void _getProperty() {
    Properties props = new Properties();
    props.getProperty("a");
  }

  static void _putAll() {
    Properties props = new Properties();
    // set all key-value pairs contained inside of a map
    props.putAll(Map.of("a", 1));
  }

  static void _setProperty() {
    Properties props = new Properties();
    props.setProperty("a", "alpha");
  }
}
