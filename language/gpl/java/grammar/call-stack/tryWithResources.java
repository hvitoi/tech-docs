class Main {
  public static void main(String[] args) {

    /**
     * Try with resources (Java 7)
     */

    try (MyConnection conn = new MyConnection()) {
      // if connection initialization fails, it will automatically invoke close()
      // this way, there is no need to implement a finally block
      conn.readData();
    } catch (Exception e) {
      e.printStackTrace();
    }

  }
}

class MyConnection implements AutoCloseable {
  public MyConnection() {
    System.out.println("Opening connection");
    throw new IllegalStateException(); // simulate failure to open connection
  }

  public void readData() {
    System.out.println("Reading data");
    throw new IllegalStateException(); // simulate failure to read data
  }

  public void close() { // This method is the requirement of AutoCloseable interface
    System.out.println("Closing connection");
  }
}
