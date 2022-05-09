import java.net.URI;
import java.net.URISyntaxException;

class Main {
  public static void main(String[] args) {
    // Static methods
    URINew.run();
    URICreate.run();

  }
}

class URINew {
  static void run() {
    try {
      URI uri = new URI("https://example.com");
    } catch (URISyntaxException e) {
    }

  }
}

class URICreate {
  static void run() {
    URI uri = URI.create("https://example.com");
  }
}