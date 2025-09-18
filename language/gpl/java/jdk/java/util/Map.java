import java.util.HashMap;
import java.util.Hashtable;
import java.util.LinkedHashMap;
import java.util.Map;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new();
    _of();

    // Instance methods
    _get();
    _put();
    _entrySet();
    _keySet();
    values();
  }

  static Map<Integer, String> _new() {
    Map<Integer, String> hashMap = new HashMap<>();
    Map<Integer, String> linkedHashMap = new LinkedHashMap<>();
    Map<Integer, String> hashtable = new Hashtable<>(); // thread-safe
    return hashMap;
  }

  static void _of() {
    Map.of("cpf", "000.000.000-00");
  }

  static void _get() {
    Map<Integer, String> map = _new();
    map.put(1, "aaa");
    map.get(1); // aaa
  }

  static void _put() {
    Map<Integer, String> map = _new();
    map.put(1, "aaa");
    map.put(2, "bbb");
  }

  static void _entrySet() {
    Map<Integer, String> map = _new();
    map.put(1, "aaa");
    for (Map.Entry<Integer, String> entry : map.entrySet()) {
      entry.getKey(); // 1
      entry.getValue(); // aaa
    }

  }

  static void _keySet() {
    Map<Integer, String> map = _new();
    map.put(1, "aaa");
    for (Integer key : map.keySet()) {
      // key = 1
    }

  }

  static void values() {
    Map<Integer, String> map = _new();
    map.put(1, "aaa");
    for (String value : map.values()) {
      // value = "aaa"
    }
  }
}
