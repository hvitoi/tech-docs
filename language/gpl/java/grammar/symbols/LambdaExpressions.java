import java.util.Optional;

class Main {
  public static void main(String[] args) {

    var msg = Optional.of("Hey!");

    msg.ifPresent(s -> System.out.println(s.length()));
    msg.ifPresent(System.out::println);

  }
}
