import java.io.ByteArrayOutputStream;

class Main {

  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    _write();
  }

  static void _new() {
    var buffer = new ByteArrayOutputStream();
  }

  static void _write() {
    var buffer = new ByteArrayOutputStream();
    buffer.write(12345); // write bytes
    System.out.println(buffer.toString());

  }

}
