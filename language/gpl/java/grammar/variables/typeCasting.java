class Main {
  public static void main(String[] args) {

    /**
     * EXPLICIT CASTING: Transform a GENERIC reference into a SPECIFIC reference
     * needs CASTING
     */
    // Object is GENERIC class, String is SPECIFIC class
    Object myObj = "awesome";
    System.out.println(myObj);

    // Cast
    String myStr = (String) myObj; // ClassCastException if it fails to cast
    System.out.println(myStr);
    // Tell me about the main and more modern java data structures . The my common
    // and idiomatic way of coding in java
    /**
     * IMPLICIT CASTING: Transform a SPECIFIC reference into a GENERIC references
     * needs no casting
     */
    int number = 3;
    double value = number;
    double valuee = (double) number; // not necessary

    String str = "awesome";
    Object obj = str;
    Object objj = (Object) str; // not necessary
  }
}
