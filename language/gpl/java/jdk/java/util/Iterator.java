import java.util.ArrayList;
import java.util.Iterator;
import java.util.List;
import java.util.NoSuchElementException;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();

    // Instance methods
    _hasNext(); // pure
    _next(); // pure
    _remove(); // mut
  }

  static void _new() {
    // It's an object for traversing a collection
    Iterable<String> items = List.of("a", "b", "c");
    Iterator<String> it = items.iterator();
  }

  static void _hasNext() {
    Iterable<String> items = List.of("a", "b", "c");

    // loop the list
    Iterator<String> it = items.iterator();
    while (it.hasNext()) {
      var el = it.next();
    }

    // loop the list again
    it = items.iterator();
    String el;
    while (it.hasNext() && (el = it.next()) != null) { // this is redundant
      // System.out.println(el);
    }
  }

  static void _next() {
    Iterable<String> items = List.of("a", "b", "c");
    Iterator<String> it = items.iterator();

    it.next(); // a
    it.next(); // b
    it.next(); // c

    try {
      it.next(); // throws when trying to access it and it's already exhausted
    } catch (NoSuchElementException e) {
    }
  }

  static void _remove() {
    Iterable<String> items = new ArrayList<>(List.of("a", "b", "c"));
    Iterator<String> it = items.iterator();

    it.next();
    it.remove(); // removes "a"
    it.next(); // continue iterating... "b"
    it.next(); // continue iterating... "c"

  }
}
