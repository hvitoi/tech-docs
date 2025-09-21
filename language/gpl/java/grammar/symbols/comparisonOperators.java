// Comparisons on primitive types compare the value
// Comparisons on objects compare the memory addresses (references) - under the hood is calls the .equals method

class Main {
  public static void main(String[] args) {

    /*
     * Primitives
     */
    var a = 1 == 1; // true

    /*
     * Objects
     */
    var p1 = new Person();
    var p2 = new Person();
    var p3 = p1;

    var b = p1 == p2; // false
    var c = p1 == p3; // true

    /*
     * Strings (Special case)
     */
    // Naturally you would think that this returns false, but string literals in
    // Java are "interned", meaning that they're stored in a pool in the JVM so that
    // identical string literals reuse the same object
    var d = "Henry" == "Henry"; // true!
    var e = new String("Henry") == new String("Henry"); // false! (you bypass the string pool)

  }
}

class Person {
}
