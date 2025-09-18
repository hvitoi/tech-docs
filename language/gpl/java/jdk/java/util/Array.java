class Main {
  public static void main(String[] args) {

    // Static Methods
    _new();

  }

  static void _new() {
    // 1D array (empty values)
    int[] scores = new int[3]; // int default value: 0
    Object[] words = new Object[3]; // obj default value: null

    // 1D array (with initial values)
    int[] numbers1 = new int[] { 1, 2, 3 };
    int[] numbers2 = { 1, 2, 3 };
    int numbers3[] = { 1, 2, 3 };
    String[] animals1 = new String[] { "cat", "dog", "bird" };
    String[] animals2 = { "cat", "dog", "bird" };
    String animals3[] = { "cat", "dog", "bird" };

    // 2D array (with initial values)
    int[][] numbers4 = new int[][] { { 1, 2, 3 }, { 4, 5, 6 } };
    int[][] numbers5 = { { 1, 2, 3 }, { 4, 5, 6 } };
    int numbers6[][] = { { 1, 2, 3 }, { 4, 5, 6 } };

    // access elements
    try {
      scores[0] = 10;
      System.out.println(scores[0]); // ok
      System.out.println(scores[9]);// exception

    } catch (ArrayIndexOutOfBoundsException e) {
    }

    // array length
    System.out.println(scores.length);

  }
}
