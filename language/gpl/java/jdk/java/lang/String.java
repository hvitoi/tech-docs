import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.stream.Collectors;
import java.util.stream.Stream;

// All String methods are pure. It's not possible to mutate a string

class Main {
  public static void main(String[] args) {
    _new();

    // Static methods
    _format();
    _join();
    _valueOf();

    // Instance methods
    _equals();
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
    _getBytes();
  }

  static void _new() {
    // String from literal. This "interns" the string, so that equal strings use the
    // same object from the string pool
    var str = "Henry";
    str = str + " Vitoi"; // concatenate (create new, strings are immutable)

    // String Class
    var str2 = new String("Henry"); // Creates a new string object, instead of "interning" it from the string pool
    var str3 = new String("Henry".getBytes(), StandardCharsets.UTF_8); // specify encoding (charset)
    var str4 = new String(new char[] { 'a', 'b', 'c' }); // from array of chars
    var str5 = new String(new byte[] { 65, 66, 67 }); // from array of bytes

    // Text Block (Java 15)
    var str6 = """
        {
          "name": "Alice",
          "email": "alice@example.com"
        }
        """;

    // String Builder: useful when building strings dynamically
    StringBuilder sb = new StringBuilder();
    var str7 = sb
        .append("Henry")
        .append(" ")
        .append("Vitoi")
        .toString();

    // Stream
    var str8 = Stream
        .of("a", "b", "c")
        .collect(Collectors.joining(","));

    // Array of Strings
    String[] strArray = { "alpha", "beta", "gamma" };
    var strArray2 = new String[] { "alpha", "beta", "gamma" };
  }

  static void _format() {
    var name = "Henry";
    var age = 30;
    var formatted = String.format("Hello, %s! You are %d years old.", name, age);
  }

  static void _join() {
    var items = List.of("alpha", "beta", "gamma");
    var joined = String.join(",", items);
  }

  static void _valueOf() {
    // Create a string out of another type
    var str = String.valueOf(123);
    var str2 = String.valueOf('a');
    var str3 = String.valueOf(new char[] { 'a', 'b', 'c' });
  }

  static void _equals() {
    // Compares the objects. In this case it is true because string literals are
    // interned and stored in a pool of strings
    var areEqual = "Henry" == "Henry"; // true!
    var areEqual2 = new String("Henry") == new String("Henry"); // false (bypass the string pool)

    // Compares the values
    var areEqual3 = "Henry".equals("Henry");
  }

  static void _charAt() {
    var s = "blue";
    s.charAt(2); // char at index 2
  }

  static void _compareTo() {
    var s1 = "blue";
    var s2 = "blue";
    var s3 = "green";

    s1.compareTo(s2); // zero
    s1.compareTo(s3); // non-zero
  }

  static void _concat() {
    var s = "hey";
    s.concat("!"); // hey!
  }

  static void _contains() {
    var s = "awesome";
    s.contains("esom"); // true
  }

  static void _isEmpty() {
    var s = "";
    s.isEmpty(); // true
  }

  static void _indexOf() {
    var s = "blue";
    s.indexOf('u'); // index of character u (first occurrence)
    s.indexOf("lu"); // index of a substring (first occurrence)
  }

  static void _length() {
    var s = "blue";
    s.length(); // string length
    for (int i = 0; i < s.length(); i++) {
      //
    }
  }

  static void _matches() {
    var email = "mail@mail.com";
    email.matches("^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\\.[a-zA-Z]{2,}$");

    var cpf = "000.000.000-00";
    cpf.matches("\\d{3}\\.\\d{3}\\.\\d{3}\\-\\d{2}");
  }

  static void _replace() {
    // original string remains untouched
    var s = "blue";
    s.replace("e", "eee");
    s.replace('e', 'i');
    s.replace("bl", "Bl");
  }

  static void _substring() {
    var s = "blue";
    // get "blu"
    s.substring(0, 3); // throws StringIndexOutOfBoundsException if out of bounds
  }

  static void _toLowerCase() {
    var s = "BLUE";
    s.toLowerCase(); // original string remains untouched
  }

  static void _toUpperCase() {
    var s = "blue";
    s.toUpperCase(); // original string remains untouched
  }

  static void _trim() {
    var s = " hey!   ";
    s.trim(); // hey!
  }

  static void _getBytes() {
    // Get an array of bytes
    var s = "Hey!";
    s.getBytes();
  }
}
