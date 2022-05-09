void main() {
  /**
   * Static
   */
  MapNew();

  /**
   * Instance
   */
  MapContainsKey();
  MapContainsValue();
}

void MapNew() {
  Map<String, int> map1 = {'alpha': 1, 'beta': 2};
  Map<String, int> map2 = Map(); // empty map
  map1['a']; // access
}

void MapContainsKey() {
  Map<String, int> map = {'alpha': 1, 'beta': 2};

  map.containsKey('alpha'); // true
}

void MapContainsValue() {
  Map<String, int> map = {'alpha': 1, 'beta': 2};

  map.containsValue(1); // true
}
