import java.lang.Comparable;

import java.util.Collections;
import java.util.Comparator;
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Set;
import java.util.HashSet;

class Main {
  public static void main(String[] args) {

    // Static methods
    _new();
    _comparing();
  }

  static void _new() {
    Comparator comparator1 = new PersonComparator(); // old way of creating comparators
    Comparator comparator2 = (a, b) -> Integer.compare(a, b); // new syntax

  }

  static void _comparing() {
    // Comparator.comparing();
  }
}

class PersonComparator implements Comparator<Integer> {

  @Override
  public int compare(Integer a, Integer b) {
    return Integer.compare(a, b); // 0: equal, -1: smaller, +1: bigger
  }

}
