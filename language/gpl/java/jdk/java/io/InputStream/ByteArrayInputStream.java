import java.io.ByteArrayInputStream;
import java.io.InputStream;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();
  }

  static void _new() {
    InputStream emptyStream = new ByteArrayInputStream(new byte[0]);
  }

}
