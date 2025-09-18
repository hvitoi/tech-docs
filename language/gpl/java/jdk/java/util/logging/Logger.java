import java.util.logging.Logger;

class Main {
  public static void main(String[] args) {
    new LoggerGetLogger().run();

  }

}

class LoggerGetLogger {
  private Logger logger = Logger.getLogger(getClass().getName());

  void run() {
    logger.info("Hey there!");
    logger.warning("Hey serious there!");
  }
}
