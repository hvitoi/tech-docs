import java.nio.charset.StandardCharsets;

class Main {
  public static void main(String[] args) {

    // Static methods
    _new();
    _format();

    // Instance methods
    _charAt();
    _compareTo();
    _concat();
    _contains();
    _isEmpty();
    _indexOf();
    _length();
    _matches();
    _replace();
    _substring();
    _toLowerCase();
    _toUpperCase();
    _trim();
  }

  static void _new() {
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

  static void _format() {
    String name = "Henry";
    String formatted = String.format("Hello, %s!", name);
  }

  static void _charAt() {
    String s = "blue";
    s.charAt(2); // char at index 2
  }

  static void _compareTo() {
    String s1 = "blue";
    String s2 = "blue";
    String s3 = "green";

    s1.compareTo(s2); // zero
    s1.compareTo(s3); // non-zero
  }

  static void _concat() {
    String s = "hey";
    s.concat("!"); // hey!
  }

  static void _contains() {
    String s = "awesome";
    s.contains("esom"); // true
  }

  static void _isEmpty() {
    String s = "";
    s.isEmpty(); // true
  }

  static void _indexOf() {
    String s = "blue";

    s.indexOf('u'); // index of character u (first occurrence)
    s.indexOf("lu"); // index of a substring (first occurrence)

  }

  static void _length() {
    String s = "blue";

    s.length(); // string length

    for (int i = 0; i < s.length(); i++) {
      s.charAt(i);
    }
  }

  static void _matches() {
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

  static void _replace() {
    String s = "blue";

    s.replace("e", "eee"); // original string remains untouched
    s.replace('e', 'i');
    s.replace("bl", "Bl");
  }

  static void _substring() {
    String s = "blue";

    // get "blu"
    s.substring(0, 3); // throws StringIndexOutOfBoundsException if out of bounds
  }

  static void _toLowerCase() {
    String s = "BLUE";
    s.toLowerCase(); // original string remains untouched
  }

  static void _toUpperCase() {
    String s = "blue";
    s.toUpperCase(); // original string remains untouched
  }

  static void _trim() {
    String s = " hey!   ";
    s.trim(); // hey!
  }
}
