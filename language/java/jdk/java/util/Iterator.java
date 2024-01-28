import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Iterator;

class Main {
  public static void main(String[] args) {
    _new();

    // Instance methods
    hasNext();
    next();
    remove();
  }

  static Iterator _new() {
    Iterable<String> list = Arrays.asList("henry", "john", "albert");
    Iterator<String> it = list.iterator(); // must be reset in order to iterate again
    return it;
  }

  static void hasNext() {
    Iterator<String> it = ListIterator.run();

    // loop the list
    while (it.hasNext()) {
      String el = it.next();
    }
  }

  static void next() {
    Iterator<String> it = ListIterator.run();

    // loop the list
    while (it.hasNext()) {
      String el = it.next(); // the current element in the loop
    }
  }

  static void remove() {
    Iterator<String> it = ListIterator.run();

    // loop the list
    while (it.hasNext()) {
      String el = it.next();
      it.remove(); // remove the current element
    }
  }
}
