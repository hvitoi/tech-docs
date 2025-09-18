import java.io.IOException;
import java.net.URI;
import java.net.URISyntaxException;
import java.net.http.HttpClient;
import java.net.http.HttpRequest;
import java.net.http.HttpResponse;

class Main {

  public static void main(String[] args) throws URISyntaxException, IOException, InterruptedException {
    // Static methods
    _newBuilder();

  }

  static void _newBuilder() throws URISyntaxException, IOException, InterruptedException {

    var uri = new URI("https://httpbin.org/get");
    var request = HttpRequest.newBuilder(uri)
        .GET()
        .build();
  }

}
