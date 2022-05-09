import 'dart:convert';

void main() {
  jsonEncode();
  jsonDecode();
}

void jsonDecode() {
  dynamic decoded = json.decode('[{"alpha":"a","beta":"b"}]');
}

void jsonEncode() {
  String encoded = json.encode([
    {"alpha": "a", "beta": "b"}
  ]);
}
