import 'dart:typed_data';

import 'package:http_interceptor/http_interceptor.dart';

void main() {
  /**
   * Instance
   */
  ResponseDataHeaders();
  ResponseDataBody();
  ResponseDataStatusCode();
}

void ResponseDataHeaders() {
  ResponseData data = ResponseData(Uint8List(99), 200);
  data.headers;
}

void ResponseDataBody() {
  ResponseData data = ResponseData(Uint8List(99), 200);
  data.body;
}

void ResponseDataStatusCode() {
  ResponseData data = ResponseData(Uint8List(99), 200);
  data.statusCode;
}
