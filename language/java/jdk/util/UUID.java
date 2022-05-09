import java.util.UUID;

class Main {
  public static void main(String[] args) {

    // Static methods
    UUIDRandomUUID.run();
  }
}

class UUIDRandomUUID {
  static void run() {
    UUID uuid = UUID.randomUUID();
  }
}