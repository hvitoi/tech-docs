import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

class Main {

  public static void main(String[] args) throws URISyntaxException, IOException, InterruptedException {
    // Static methods
    _newHttpClient();

    // Instance methods
    _send();

  }

  static void _newHttpClient() {
    var httpClient = HttpClient.newHttpClient();
  }

  static void _send() throws URISyntaxException, IOException, InterruptedException {
    var httpClient = HttpClient.newHttpClient();

    var request = HttpRequest.newBuilder()
        .uri(URI.create("https://httpbin.org/get"))
        .GET()
        .build();

    var response = httpClient.send(request, HttpResponse.BodyHandlers.discarding());
    System.out.println(response.statusCode());
  }

}
