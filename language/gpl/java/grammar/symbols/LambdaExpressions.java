import java.util.List;

class Main {
  public static void main(String[] args) {

    var colors = List.of("red", "green", "blue");
    colors.stream()
        .filter(c -> c.startsWith("g"))
        .forEach(System.out::println);

  }
}
