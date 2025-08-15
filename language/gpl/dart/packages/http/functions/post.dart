import 'package:http/http.dart';

void main() async {
  var url = Uri.parse('https://animechan.vercel.app/api/quotes');

  // get
  Response res = await post(
    Uri.https('example.com', 'whatsit/create'),
    headers: {'Content-type': 'application/json'},
    body: {'name': 'doodle', 'color': 'blue'},
  );
}
