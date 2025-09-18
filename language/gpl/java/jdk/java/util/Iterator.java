import java.util.Arrays;
import java.util.Iterator;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    _hasNext();
    _next();
    _remove();
  }

  static Iterator<String> _new() {
    Iterable<String> list = Arrays.asList("henry", "john", "albert");
    Iterator<String> it = list.iterator(); // must be reset in order to iterate again
    return it;
  }

  static void _hasNext() {
    Iterator<String> it = _new();

    // loop the list
    while (it.hasNext()) {
      String el = it.next();
    }
  }

  static void _next() {
    Iterator<String> it = _new();
    // loop the list
    while (it.hasNext()) {
      String el = it.next(); // the current element in the loop
    }
  }

  static void _remove() {
    Iterator<String> it = _new();
    // loop the list
    while (it.hasNext()) {
      String el = it.next();
      it.remove(); // remove the current element
    }
  }
}
