import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.regex.Pattern;

class Main {
  public static void main(String[] args) {
    /**
     * Static
     */
    PatternCompile.run();

  }
}

class PatternCompile {
  static void run() {
    Pattern pattern = Pattern.compile("abc*");
  }
}
