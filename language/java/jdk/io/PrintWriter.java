import java.io.PrintWriter;
import java.io.StringWriter;

class Main {
  public static void main(String[] args) {
    // Static methods
    PrintWriterNew.run();
  }
}

class PrintWriterNew {
  static void run() {
    StringWriter sw = new StringWriter();
    PrintWriter pw = new PrintWriter(sw);

    try {
      Integer a = 0 / 0;
    } catch (ArithmeticException e) {
      e.printStackTrace(pw);
      System.out.println(sw.toString());
    }

  }
}