import java.net.URI;
import java.net.URISyntaxException;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();
    _create();
  }

  static void _new() {
    try {
      URI uri = new URI("https://example.com");
    } catch (URISyntaxException e) {
    }

  }

  static void _create() {
    URI uri = URI.create("https://example.com");
  }
}
