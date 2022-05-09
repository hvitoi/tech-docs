import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Main {
  public static void main(String[] args) {

    List<String> list = new ArrayList<>(Arrays.asList("hey", "there"));

    for (String el : list) {
      System.out.println(el);
    }

  }
}
