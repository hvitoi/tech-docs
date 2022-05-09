import java.util.List;
import java.util.ArrayList;
import java.lang.String;

class Main {
  public static void main(String[] args) {

    List<String> list = new ArrayList<>();
    list.add("hey");
    list.add("there");

    for (int i = 0; i < list.size(); i++) {
      System.out.println(list.get(i));
    }

  }
}
