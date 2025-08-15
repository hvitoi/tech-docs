import 'package:http/http.dart';

void main() async {
  var url = Uri.parse('https://animechan.vercel.app/api/quotes');

  // get
  Response res = await get(url);

  // get with timeout (from Tuture API)
  Response res2 = await get(url).timeout(Duration(seconds: 5));
}
