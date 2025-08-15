void main() {
  /**
   * Static
   */
  IterableNew();

  /**
   * Instance
   */
  IterableToList();
}

Iterable<String> IterableNew() {
  Iterable<String> foo = ['a', 'b', 'c'];
  return foo;
}

void IterableToList() {
  Iterable<String> it = IterableNew();

  List<String> list = it.toList();
}
