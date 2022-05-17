import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

class Main {
  public static void main(String[] args) throws SQLException {
    /**
     * Static
     */
    DriverManagerGetConnection.run();

  }
}

class DriverManagerGetConnection {
  static void run() throws SQLException {
    // Uses a JDBC driver implementation
    // E.g., org.xerial:sqlite-jdbc
    Connection conn = DriverManager.getConnection("jdbc:sqlite:users_database.db");

  }
}
