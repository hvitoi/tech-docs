// A set of null-safe helpers for Objects

import java.util.Objects;

class Main {

  public static void main(String[] args) {
    // Static methods
    _toString();
    _equals();
    _hash();
  }

  static void _toString() {
    // calls the .toString method of a given Object
    // Falls back to "default" if it is null
    Objects.toString(123, "default");
  }

  static void _equals() {
    // calls the .equals method of a given Object
    // Safely compare null values of either side
    Objects.equals(1, 1); // true
    Objects.equals(1, null); // false
    Objects.equals(null, null); // true
  }

  static void _hash() {
    // Generates a hash code for a sequence of input values. The hash code is
    // generated as if all the input values were placed into an array, and that
    // array were hashed by calling Arrays.hashCode(Object []).
    Objects.hash("Henry", "Vitoi");
  }

}
