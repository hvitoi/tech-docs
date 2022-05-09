void main() {
  /**
   * Static
   */
  StringNew();

  /**
   * Instance
   */
  StringIsEmpty();
  StringSubstring();
}

String StringNew() {
  String str = 'Hello there' + ', hi!';

  // String interpolation
  String stringTemplate = '$str is the first. ${str} is the second';

  return str;
}

void StringIsEmpty() {
  var str = "hello";
  str.isEmpty; // false
}

void StringSubstring() {
  var str = "hello";
  str.substring(0, 1); // from index 0 to index 1 (excluded)
}
