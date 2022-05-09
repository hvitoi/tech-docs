void main() {
  nullNew();
}

void nullNew() {
  String a = 'hello';
  // a = null; // fail! null safety

  String? b = 'hello';
  b = null; // ok!
}
