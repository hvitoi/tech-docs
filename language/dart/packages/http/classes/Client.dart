import 'package:http/http.dart' as http;

import 'dart:convert';

void main() {
  /**
   * Static
   */
  ClientNew();

  /**
   * Instance
   */
  ClientGet();
  ClientPost();
  ClientClose();
}

void ClientNew() async {
  var client = http.Client();
}

void ClientGet() async {
  var client = http.Client();

  var res = await client.get(Uri.https('example.com', 'whatsit/create'));
}

void ClientPost() async {
  var client = http.Client();

  var res = await client.post(
    Uri.https('example.com', 'whatsit/create'),
    headers: {'Content-type': 'application/json'},
    body: {'name': 'doodle', 'color': 'blue'},
  );
}

void ClientClose() async {
  var client = http.Client();

  try {
    var response = await client.post(
      Uri.https('example.com', 'whatsit/create'),
      body: {'name': 'doodle', 'color': 'blue'},
    );
    var decodedResponse = jsonDecode(utf8.decode(response.bodyBytes)) as Map;
  } finally {
    client.close();
  }
}
