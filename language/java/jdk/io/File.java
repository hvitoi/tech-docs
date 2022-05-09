import java.io.File;

class Main {
  public static void main(String[] args) {
    // Static methods
    FileNew.run();
  }
}

class FileNew {
  static void run() {
    System.out.println("a");
    new File("sample.json"); // scoped to the root project path
  }
}
