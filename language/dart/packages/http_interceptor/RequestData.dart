import 'package:http_interceptor/http_interceptor.dart';

void main() {
  /**
   * Instance
   */
  RequestDataHeaders();
  RequestDataBody();
  RequestDataUrl();
}

void RequestDataHeaders() {
  RequestData data = RequestData(method: Method.GET, baseUrl: "example.com");
  data.headers;
}

void RequestDataBody() {
  RequestData data = RequestData(method: Method.GET, baseUrl: "example.com");
  data.body;
}

void RequestDataUrl() {
  RequestData data = RequestData(method: Method.GET, baseUrl: "example.com");
  data.url;
}
