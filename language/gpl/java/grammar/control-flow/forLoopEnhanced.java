import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

class Main {
  public static void main(String[] args) {

    List<String> list = new ArrayList<>(List.of("hey", "there"));

    // Enhanced for-loop
    for (String el : list) {
      System.out.println(el);
    }

    // Iterable forEach
    list.forEach(System.out::println);

    // Stream processing
    list.stream()
        .filter(s -> s.length() > 1)
        .map(String::toUpperCase)
        .forEach(System.out::println);

  }
}
