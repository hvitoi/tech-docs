import 'package:http/http.dart';

main() {
  /**
   * Instance
   */
  ResponseStatusCode();
  ResponseBody();
}

void ResponseStatusCode() async {
  Response res =
      await get(Uri.parse('https://animechan.vercel.app/api/quotes'));

  res.statusCode;
}

void ResponseBody() async {
  Response res =
      await get(Uri.parse('https://animechan.vercel.app/api/quotes'));

  res.body;
}
