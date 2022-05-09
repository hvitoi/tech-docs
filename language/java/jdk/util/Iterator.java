import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Iterator;

class Main {
  public static void main(String[] args) {
    ListIterator.run();

    // Instance methods
    IteratorHasNext.run();
    IteratorNext.run();
    IteratorRemove.run();
  }
}

class ListIterator {
  static Iterator run() {
    Iterable<String> list = Arrays.asList("henry", "john", "albert");
    Iterator<String> it = list.iterator(); // must be reset in order to iterate again
    return it;
  }
}

class IteratorHasNext {
  static void run() {
    Iterator<String> it = ListIterator.run();

    // loop the list
    while (it.hasNext()) {
      String el = it.next();
    }
  }
}

class IteratorNext {
  static void run() {
    Iterator<String> it = ListIterator.run();

    // loop the list
    while (it.hasNext()) {
      String el = it.next(); // the current element in the loop
    }
  }
}

class IteratorRemove {
  static void run() {
    Iterator<String> it = ListIterator.run();

    // loop the list
    while (it.hasNext()) {
      String el = it.next();
      it.remove(); // remove the current element
    }
  }
}