import java.nio.charset.StandardCharsets;

class Main {
  public static void main(String[] args) {

    // Static methods
    StringNew.run();
    StringFormat.run();

    // Instance methods
    StringCharAt.run();
    StringCompareTo.run();
    StringConcat.run();
    StringContains.run();
    StringIsEmpty.run();
    StringIndexOf.run();
    StringLength.run();
    StringMatches.run();
    StringReplace.run();
    StringSubstring.run();
    StringToLowerCase.run();
    StringToUpperCase.run();
    StringTrim.run();
  }
}

class StringNew {
  static void run() {
    // String initialization with object literal
    String str = "My String"; // new String("My String")

    // Concatenate string
    // In order to modify a string, a new one is create (strings are immutable)
    str = str + "Append new information";

    // Create string in a specified encoding
    String englishString = "Develop with pleasure";
    byte[] englishBytes = englishString.getBytes();
    String utf8EncondedEnglishString = new String(englishBytes, StandardCharsets.UTF_8);

  }
}

class StringFormat {
  static void run() {
    String name = "Henry";
    String formatted = String.format("hello, %s!", name);
  }
}

class StringCharAt {
  static void run() {
    String s = "blue";
    s.charAt(2); // char at index 2
  }
}

class StringCompareTo {
  static void run() {
    String s1 = "blue";
    String s2 = "blue";
    String s3 = "green";

    s1.compareTo(s2); // zero
    s1.compareTo(s3); // non-zero
  }
}

class StringConcat {
  static void run() {
    String s = "hey";
    s.concat("!"); // hey!
  }
}

class StringContains {
  static void run() {
    String s = "awesome";
    s.contains("esom"); // true
  }
}

class StringIsEmpty {
  static void run() {
    String s = "";
    s.isEmpty(); // true
  }
}

class StringIndexOf {
  static void run() {
    String s = "blue";

    s.indexOf('u'); // index of character u (first occurrence)
    s.indexOf("lu"); // index of a substring (first occurrence)

  }
}

class StringLength {
  static void run() {
    String s = "blue";

    s.length(); // string length

    for (int i = 0; i < s.length(); i++) {
      s.charAt(i);
    }

  }
}

class StringMatches {
  static void run() {
    String email = "mail@mail.com";
    email.matches("^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$");

    String cpf = "000.000.000-00";
    cpf.matches("\\d{3}\\.\\d{3}\\.\\d{3}\\-\\d{2}");

    // if (ddd == null || numero == null) {
    // throw new IllegalArgumentException("DDD e Numero sao obrigatorios!");
    // }

    // String ddd = "32";
    // String numero = "963400122";
    // ddd.matches("\\d{2}");
    // numero.matches("\\d{8}|\\d{9}");

  }
}

class StringReplace {
  static void run() {
    String s = "blue";

    s.replace("e", "eee"); // original string remains untouched
    s.replace('e', 'i');
    s.replace("bl", "Bl");

  }
}

class StringSubstring {
  static void run() {
    String s = "blue";

    // get "blu"
    s.substring(0, 3); // throws StringIndexOutOfBoundsException if out of bounds

  }
}

class StringToLowerCase {
  static void run() {
    String s = "BLUE";

    s.toLowerCase(); // original string remains untouched

  }
}

class StringToUpperCase {
  static void run() {
    String s = "blue";

    s.toUpperCase(); // original string remains untouched

  }
}

class StringTrim {
  static void run() {
    String s = " hey!   ";

    s.trim(); // hey!

  }
}
