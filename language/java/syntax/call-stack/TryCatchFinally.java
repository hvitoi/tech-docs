import java.sql.Connection;

class Main {
  public static void main(String[] args) {

    try {
      int a = 9 / 0;
    } catch (NullPointerException e) { // will not catch because it's not a NullPointException
      System.out.println(e);
    } catch (IllegalArgumentException e) {
      System.out.println(e);
    } catch (ArrayIndexOutOfBoundsException | ArithmeticException e) { // will catch because it's ArithmeticExpection
      System.out.println(e);
      System.out.println(e.getMessage());
      e.printStackTrace();
    } catch (Exception e) { // catch all the rest
      System.out.println(e);
    } finally {
      System.out.println("I will run on success or failure."); // usually to close db connection
    }

    System.out.println("Rest of the code.");

    // ---

    /**
     * Try with resources
     */

    try (MyConnection conn = new MyConnection()) {
      // if connection initialization fails, it will automatically invoke close()
      // this way, there is no need to implement a finally block
      conn.readData();
    } catch (Exception e) {
      e.printStackTrace();
    }

    System.out.println("Rest of the code.");

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