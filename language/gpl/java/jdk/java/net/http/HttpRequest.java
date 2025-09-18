import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

class Main {

  public static void main(String[] args) {
    // Static methods
    _newBuilder();
    _BodyPublishers_ofString();

  }

  static void _newBuilder() {

    var getRequest = HttpRequest.newBuilder(URI.create("https://httpbin.org/get"))
        .GET()
        .build();

    var body = """
        {
          "name": "Alice",
          "email": "alice@example.com"
        }
        """;
    var postRequest = HttpRequest.newBuilder()
        .uri(URI.create("https://httpbin.org/post"))
        .header("Content-Type", "application/json")
        .POST(HttpRequest.BodyPublishers.ofString(body))
        .build();

  }

  static void _BodyPublishers_ofString() {

    // Receive the Request Body as a string

    var body = """
        {
          "name": "Alice",
          "email": "alice@example.com"
        }
        """;
    var postRequest = HttpRequest.newBuilder()
        .uri(URI.create("https://httpbin.org/post"))
        .header("Content-Type", "application/json")
        .POST(HttpRequest.BodyPublishers.ofString(body))
        .build();

  }

}
