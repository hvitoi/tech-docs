import java.util.logging.Logger;

class Main {
  public static void main(String[] args) {
    // Static methods
    _getLogger();

    // Instance methods
    _info();
    _warning();
  }

  static void _getLogger() {
    // Logger logger = Logger.getLogger(getClass().getName());
    Logger logger = Logger.getLogger(Main.class.getName());
  }

  static void _info() {
    Logger logger = Logger.getLogger(Main.class.getName());
    logger.info("Hey there!");
  }

  static void _warning() {
    Logger logger = Logger.getLogger(Main.class.getName());
    logger.warning("Hey serious there!");
  }

}
