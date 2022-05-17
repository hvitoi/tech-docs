import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Map;
import java.util.Properties;

class Main {
  public static void main(String[] args) {
    /**
     * Static
     */
    PropertiesNew.run();

    /**
     * Instance
     */
    PropertiesSetProperty.run();
    PropertiesGetProperty.run();
    PropertiesPutAll.run();

  }
}

class PropertiesNew {
  static void run() {
    Properties props = new Properties();
  }
}

class PropertiesSetProperty {
  static void run() {
    Properties props = new Properties();

    props.setProperty("a", "alpha");
  }
}

class PropertiesGetProperty {
  static void run() {
    Properties props = new Properties();

    props.getProperty("a");
  }
}

class PropertiesPutAll {
  static void run() {
    Properties props = new Properties();

    // set all key-value pairs contained inside of a map
    props.putAll(Map.of("a", 1));
  }
}
