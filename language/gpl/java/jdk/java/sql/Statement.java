import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

class Main {
  public static void main(String[] args) throws SQLException {
    /**
     * Static
     */
    _new();

    /**
     * Instance
     */
    _execute();
  }

  static Statement _new() throws SQLException {
    Connection conn = DriverManager.getConnection("jdbc:sqlite:user_database.db");
    Statement statement = conn.createStatement();
    return statement;
  }

  static void _execute() throws SQLException {
    Statement statement = _new();
    statement.execute("CREATE TABLE user (uuid varchar(200) primary key, email varchar(200))");
  }
}
