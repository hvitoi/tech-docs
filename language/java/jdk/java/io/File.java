import java.io.File;
import java.nio.file.Path;

class Main {
  public static void main(String[] args) {
    /**
     * Static
     */
    FileNew.run();

    /**
     * Instance
     */
    FileToPath.run();
    FileGetParentFile.run();
    FileGetMkdirs.run();
  }
}

class FileNew {
  static File run() {
    File file = new File("src/main/resources/sample.json"); // scoped to the root project path
    return file;
  }
}

class FileToPath {
  static void run() {
    File file = FileNew.run();

    Path path = file.toPath();
  }
}

class FileGetParentFile {
  static void run() {
    File file = FileNew.run();

    // the same filename but at a parent directory
    File parentFile = file.getParentFile();
  }
}

class FileGetMkdirs {
  static void run() {
    File file = FileNew.run();

    // create parent directories as needed to create the file
    file.mkdirs();
  }
}
