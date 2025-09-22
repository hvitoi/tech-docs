import java.io.IOException;
import java.net.URI;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

class Main {

  public static void main(String[] args) {
    _new();

    // Static methods
    _BodyHandlers_ofString();
    _BodyHandlers_discarding();

    // Instance methods
    _statusCode();
    _body();
  }

  static HttpResponse<String> _new() {
    var httpClient = HttpClient.newHttpClient();
    var request = HttpRequest.newBuilder()
        .uri(URI.create("https://httpbin.org/get"))
        .GET()
        .build();
    HttpResponse<String> response = null;
    try {
      response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
    } catch (IOException | InterruptedException e) {
      e.printStackTrace();
    }
    return response;
  }

  static void _BodyHandlers_ofString() {
    var httpClient = HttpClient.newHttpClient();
    var request = HttpRequest.newBuilder()
        .uri(URI.create("https://httpbin.org/get"))
        .GET()
        .build();
    try {
      // Treat the response body as a String
      var response = httpClient.send(request, HttpResponse.BodyHandlers.ofString());
    } catch (IOException | InterruptedException e) {
      e.printStackTrace();
    }

  }

  static void _BodyHandlers_discarding() {
    var httpClient = HttpClient.newHttpClient();
    var request = HttpRequest.newBuilder()
        .uri(URI.create("https://httpbin.org/get"))
        .GET()
        .build();
    try {
      // Ignore the response body
      var response = httpClient.send(request, HttpResponse.BodyHandlers.discarding());
    } catch (IOException | InterruptedException e) {
      e.printStackTrace();
    }

  }

  static void _statusCode() {
    var response = _new();
    var responseStatusCode = response.statusCode();
  }

  static void _body() {
    // The response body
    var response = _new();
    var responseBody = response.body();
  }

}
