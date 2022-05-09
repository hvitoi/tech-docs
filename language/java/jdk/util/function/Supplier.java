import java.util.function.Supplier;

// Void -> One Output

class Main {
  public static void main(String[] args) {

    // Static methods
    SupplierNew.run();

    // Instance methods
    SupplierGet.run();

  }
}

class SupplierNew {
  static void run() {
    // Supplier of results
    Supplier<String> supplier = () -> "Hello";

  }
}

class SupplierGet {
  static void run() {
    Supplier<String> supplier = () -> "Hello";
    String res = supplier.get(); // hello
  }
}