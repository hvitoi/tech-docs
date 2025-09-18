import java.util.HashMap;
import java.util.Hashtable;
import java.util.LinkedHashMap;
import java.util.Map;

class Main {
  public static void main(String[] args) {

    /**
     * Implementations
     */
    // Implementations
    implementations();

    /**
     * Static
     */
    _new();
    of();

    /**
     * Instance
     */
    put();
    _get();
    entrySet();
    keySet();
    values();

  }

  static void implementations() {
    Map<Integer, String> hashMap = new HashMap<>();
    Map<Integer, String> linkedHashMap = new LinkedHashMap<>();
    Map<Integer, String> hashtable = new Hashtable<>(); // thread-safe
  }

  static Map<Integer, String> _new() {
    Map<Integer, String> map = new HashMap<>();
    return map;
  }

  static void of() {
    Map.of("cpf", "000.000.000-00");
  }

  static void put() {
    Map<Integer, String> map = MapNew.run();
    map.put(1, "aaa");
    map.put(2, "bbb");
  }

  static void get() {
    Map<Integer, String> map = MapNew.run();
    map.put(1, "aaa");
    map.get(1); // aaa
  }

  static void entrySet() {
    Map<Integer, String> map = MapNew.run();
    map.put(1, "aaa");

    for (Map.Entry<Integer, String> entry : map.entrySet()) {
      entry.getKey(); // 1
      entry.getValue(); // aaa
    }

  }

  static void keySet() {
    Map<Integer, String> map = MapNew.run();
    map.put(1, "aaa");

    for (Integer key : map.keySet()) {
      // key = 1
    }

  }

  static void values() {
    Map<Integer, String> map = MapNew.run();
    map.put(1, "aaa");

    for (String value : map.values()) {
      // value = "aaa"
    }

  }
}
