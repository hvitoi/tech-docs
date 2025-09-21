class Main {
  public static void main(String[] args) {
    _new();

    // Static Methods
    _valueOf();
    _isLetter();
  }

  static void _new() {
    // Stores a single unicode character
    char myChar1 = 'A';
    Character myChar2 = 'A';
  }

  static void _valueOf() {
    Character ref = Character.valueOf('a');
  }

  static void _isLetter() {
    boolean foo = Character.isLetter('a'); // true
    boolean bar = Character.isLetter('2'); // false
  }
}
