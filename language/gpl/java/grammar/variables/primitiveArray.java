class Main {
  public static void main(String[] args) {
    create();
    access();
    length();
  }

  static void create() {
    // Integer array
    int[] intArray = { 1, 2, 3 };
    int intArray2[] = { 1, 2, 3 }; // old syntax, avoid it!
    var intArray3 = new int[] { 1, 2, 3 };
    var intArray4 = new int[3]; // declaration only. All 3 elements are initialized to 0
    var intMatrix5 = new int[][] { { 1, 2, 3 }, { 4, 5, 6 }, { 7, 8, 9 } }; // 2D array

    // Char array
    char[] charArray = { 'a', 'b', 'c' };
    var charArray2 = new char[] { 'a', 'b', 'c' };

    // Byte array
    byte[] byteArray = { 65, 66, 67 };
    var byteArray2 = new byte[] { 65, 66, 67 };

    // String array
    String[] strArray = { "alpha", "beta", "gamma" };
    var strArray2 = new String[] { "alpha", "beta", "gamma" };

    // Object array
    var words = new Object[3]; // obj default value: null
  }

  static void access() {
    var data = new int[] { 10, 20, 30 };

    // Okay
    data[0] = 10;

    // Throws!
    try {
      data[9] = 10;
    } catch (ArrayIndexOutOfBoundsException e) {
    }

  }

  static void length() {
    var data = new int[] { 10, 20, 30 };
    System.out.println(data.length);
  }
}
