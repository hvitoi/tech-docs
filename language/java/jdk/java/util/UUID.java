import java.util.UUID;

class Main {
  public static void main(String[] args) {

    // Static methods
    UUIDRandomUUID.run();
    UUIDFromString.fromString();
  }
}

class UUIDRandomUUID {
  static void run() {
    UUID uuid = UUID.randomUUID();
  }
}

class UUIDFromString {
  static void run() {
    UUID uuid = UUID.fromString("123e4567-e89b-12d3-a456-426614174000");
  }
}