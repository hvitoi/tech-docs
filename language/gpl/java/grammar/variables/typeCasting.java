class Main {
  public static void main(String[] args) {

    /**
     * EXPLICIT CASTING
     */
    Object obj = "Henry";
    String str = (String) obj; // Object (Generic) -> String (Specific)

    /**
     * IMPLICIT CASTING
     */
    String myStr = "awesome"; // String (Specific) -> Object (Generic)
    Object myObj = myStr;
    Object myObjj = (Object) myStr; // not necessary

  }
}
