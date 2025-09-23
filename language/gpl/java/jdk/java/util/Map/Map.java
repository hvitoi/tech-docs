import java.util.HashMap;
import java.util.Hashtable;
import java.util.LinkedHashMap;
import java.util.Map;

class Main {
  public static void main(String[] args) {
    // Static methods
    _new(); // -> Map<K,V>
    _of(); // -> Map<K,V>

    // Instance methods
    _get(); // pure (-> V)
    _put(); // mut (-> V)
    _entrySet(); // pure (-> Set<Entry<K,V>>)
    _keySet(); // pure (-> Set<K>)
    _values(); // pure (-> Collection<V>)
  }

  static void _new() {
    Map<Integer, String> hashMap = new HashMap<>();
    Map<Integer, String> linkedHashMap = new LinkedHashMap<>();
    Map<Integer, String> hashtable = new Hashtable<>(); // thread-safe
  }

  static void _of() {
    // Immutable
    var map = Map.of("a", "alpha");
  }

  static void _get() {
    var map = Map.of("a", "alpha");
    String value = map.get("a"); // alpha
  }

  static void _put() {
    var map = new HashMap<>(Map.of("a", "alpha"));

    // Returns the old value
    var oldValue = map.put("b", "beta");
  }

  static void _entrySet() {
    var map = new HashMap<>(Map.of("a", "alpha", "b", "beta"));

    // Good for iterating! Returns a set of entries (with key-val)
    for (var entry : map.entrySet()) {
      String key = entry.getKey();
      String value = entry.getValue();
    }
  }

  static void _keySet() {
    var map = new HashMap<>(Map.of("a", "alpha"));
    // Return a set of keys
    for (var key : map.keySet()) {
    }
  }

  static void _values() {
    var map = new HashMap<>(Map.of("a", "alpha"));
    // Return a collection of values
    for (var value : map.values()) {
    }
  }
}
