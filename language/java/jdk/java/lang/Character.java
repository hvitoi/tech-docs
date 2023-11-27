class Main {
  public static void main(String[] args) {
    // Static Methods
    _new.run();
    _valueOf.run();
    _isLetter.run();

  }
}

class _new {
  static void run() {
    // Stores unicode characters
    char myChar = 'D'; // Stores only one character
    char myUnicodeChar = '\u0044'; // D in unicode
    char myCopyrightChar = '\u00A9';
  }
}

class _valueOf {
  static void run() {
    Character ref = Character.valueOf('a');
  }
}

class _isLetter {
  static void run() {
    boolean foo = Character.isLetter('a'); // true
    boolean bar = Character.isLetter('2'); // false

  }
}
