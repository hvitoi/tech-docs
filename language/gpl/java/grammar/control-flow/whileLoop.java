import java.util.List;

class Main {
  public static void main(String[] args) {

    var items = List.of("a", "b", "c");
    var it = items.iterator();
    while (it.hasNext()) {
      var el = it.next();
    }

    // variable is assigned inside the loop's condition
    int i = 0;
    String el;
    while (i < items.size() && !(el = items.get(i)).equals("c")) {
      // Stops when it sees an element "c"
      System.out.println(el);
      i++;
    }
  }
}
