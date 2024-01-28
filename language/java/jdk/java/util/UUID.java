import java.util.UUID;

class Main {
  public static void main(String[] args) {

    // Static methods
    randomUUID();
    fromString();
  }

  static void randomUUID() {
    UUID uuid = UUID.randomUUID();
  }

  static void fromString() {
    UUID uuid = UUID.fromString("123e4567-e89b-12d3-a456-426614174000");
  }
}
