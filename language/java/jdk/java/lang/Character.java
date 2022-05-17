class Main {
  public static void main(String[] args) {
    // Static Methods
    CharacterNew.run();
    CharacterValueOf.run();

  }
}

class CharacterNew {
  static void run() {
    // Stores unicode characters
    char myChar = 'D'; // Stores only one character
    char myUnicodeChar = '\u0044'; // D in unicode
    char myCopyrightChar = '\u00A9';
  }
}

class CharacterValueOf {
  static void run() {
    Character ref = Character.valueOf('a');
  }
}
