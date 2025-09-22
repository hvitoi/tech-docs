import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

class Main {

  public static void main(String[] args) {
    // Static methods
    _newHttpClient();

    // Instance methods
    _send();
    _sendAsync();
  }

  static void _newHttpClient() {
    var httpClient = HttpClient.newHttpClient();
  }

  static void _send() {
    var httpClient = HttpClient.newHttpClient();
    var request = HttpRequest.newBuilder()
        .uri(URI.create("https://httpbin.org/get"))
        .GET()
        .build();
    try {
      var response = httpClient.send(request, HttpResponse.BodyHandlers.discarding());
    } catch (IOException | InterruptedException e) {
      e.printStackTrace();
    }
  }

  static void _sendAsync() {
    var httpClient = HttpClient.newHttpClient();
    var request = HttpRequest.newBuilder()
        .uri(URI.create("https://httpbin.org/get"))
        .GET()
        .build();
    var response = httpClient.sendAsync(request, HttpResponse.BodyHandlers.discarding())
        .thenApply(HttpResponse::statusCode)
        .thenAccept(System.out::println)
        .join();

  }

}
