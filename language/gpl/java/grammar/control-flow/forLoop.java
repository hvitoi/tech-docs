import java.util.List;
import java.util.ArrayList;
import java.lang.String;

class Main {
  public static void main(String[] args) {

    var items = new ArrayList<>(List.of("a", "b", "c"));

    for (int i = 0; i < items.size(); i++) {
      System.out.println(items.get(i));
    }

    for (int i = items.size() - 1; i >= 0; i--) {
      System.out.println(items.get(i));
    }

  }
}
