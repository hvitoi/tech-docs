class Main {
  public static void main(String[] args) {
    // Static Methods
    _new();
    _valueOf();
    _isLetter();
  }

  static void _new() {
    // Stores unicode characters
    char myChar = 'D'; // Stores only one character
    char myUnicodeChar = '\u0044'; // D in unicode
    char myCopyrightChar = '\u00A9';
  }

  static void _valueOf() {
    Character ref = Character.valueOf('a');
  }

  static void _isLetter() {
    boolean foo = Character.isLetter('a'); // true
    boolean bar = Character.isLetter('2'); // false

  }
}
