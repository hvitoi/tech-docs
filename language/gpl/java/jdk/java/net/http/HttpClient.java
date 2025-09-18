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
    _newBuilder();

  }

  static HttpClient _newHttpClient() {
    var httpClient = HttpClient.newHttpClient();
    return httpClient;
  }

  static void _send() throws URISyntaxException, IOException, InterruptedException {
    var httpClient = _newHttpClient();

    var uri = new URI("https://httpbin.org/get");
    var request = HttpRequest.newBuilder(uri)
        .GET()
        .build();

    var response = httpClient.send(request, HttpResponse.BodyHandlers.discarding());
    System.out.println(response.statusCode());
  }

}
