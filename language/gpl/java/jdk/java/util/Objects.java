import java.util.Objects;

class Main {

  public static void main(String[] args) {
    // Static methods
    _toString();
  }

  static void _toString() {
    // Convert an object to a string
    var str = Objects.toString(123, "default");
  }

}
