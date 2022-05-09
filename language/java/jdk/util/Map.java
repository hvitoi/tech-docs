import java.util.HashMap;
import java.util.Hashtable;
import java.util.LinkedHashMap;
import java.util.Map;

class Main {
  public static void main(String[] args) {

    // Implementations
    MapImplementations.run();

    // Static methods
    MapNew.run();
    MapOf.run();

    // Instance methods
    MapPut.run();
    MapGet.run();
    MapEntrySet.run();
    MapKeySet.run();
    MapValues.run();

  }
}

class MapImplementations {
  static void run() {
    Map<Integer, String> hashMap = new HashMap<>();
    Map<Integer, String> linkedHashMap = new LinkedHashMap<>();
    Map<Integer, String> hashtable = new Hashtable<>(); // thread-safe
  }
}

class MapNew {
  static Map<Integer, String> run() {
    Map<Integer, String> map = new HashMap<>();
    return map;
  }
}

class MapOf {
  static void run() {
    Map.of("cpf", "000.000.000-00");
  }
}

class MapPut {
  static void run() {
    Map<Integer, String> map = MapNew.run();
    map.put(1, "aaa");
    map.put(2, "bbb");
  }
}

class MapGet {
  static void run() {
    Map<Integer, String> map = MapNew.run();
    map.put(1, "aaa");
    map.get(1); // aaa
  }
}

class MapEntrySet {
  static void run() {
    Map<Integer, String> map = MapNew.run();
    map.put(1, "aaa");

    for (Map.Entry<Integer, String> entry : map.entrySet()) {
      entry.getKey(); // 1
      entry.getValue(); // aaa
    }

  }
}

class MapKeySet {
  static void run() {
    Map<Integer, String> map = MapNew.run();
    map.put(1, "aaa");

    for (Integer key : map.keySet()) {
      // key = 1
    }

  }
}

class MapValues {
  static void run() {
    Map<Integer, String> map = MapNew.run();
    map.put(1, "aaa");

    for (String value : map.values()) {
      // value = "aaa"
    }

  }
}