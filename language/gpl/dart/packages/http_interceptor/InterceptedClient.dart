import 'dart:convert';

import 'package:http/http.dart';
import 'package:http_interceptor/http_interceptor.dart';

import 'InterceptorContract.dart';

/**
 * Defines a http client using interceptors
 */

void main() {
  /**
   * Static
   */
  InterceptedClientBuild();
}

void InterceptedClientBuild() async {
  Client client = InterceptedClient.build(
    interceptors: [LoggingInterceptor()],
    requestTimeout: Duration(seconds: 5), // default timeout
  );

  // optionally use string.toUri()
  var url = Uri.parse('https://animechan.vercel.app/api/quotes');

  // the request/response will be logged
  Response res = await client.get(url /*, params: {'id': "0"}*/);
}
