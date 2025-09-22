import java.io.ByteArrayOutputStream;
import java.io.IOException;
import java.io.InputStream;
import java.nio.charset.StandardCharsets;

class Main {

  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    _read();
    _close();
  }

  static void _new() {
    // Standard Input (stdio)
    InputStream stdin = System.in;

    // System.in itself should not be closed manually, because it's a shared
    // standard input stream managed by the JVM. Closing it can cause issues
    // elsewhere in your program.

  }

  static void _read() {
    InputStream stdio = System.in;
    try (var buffer = new ByteArrayOutputStream()) {
      int byteData;
      while ((byteData = stdio.read()) != -1) {
        if (byteData == '\n') {
          break;
        }
        buffer.write(byteData);
      }
      var result = buffer.toString(StandardCharsets.UTF_8);
      System.out.println("You entered: " + result);
      // Do NOT close System.in here
    } catch (IOException e) {
      e.printStackTrace();
    }
  }

  static void _close() {
    InputStream inputStream = System.in;
    try {
      inputStream.close();
    } catch (IOException e) {
      e.printStackTrace();
    }

  }

}
