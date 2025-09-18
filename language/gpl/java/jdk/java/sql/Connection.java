import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
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
    _createStatement();
    _prepareStatement();
  }

  static Connection _new() throws SQLException {
    Connection conn = DriverManager.getConnection("jdbc:sqlite:user_database.db");
    return conn;
  }

  static void _createStatement() throws SQLException {
    Connection conn = _new();

    // Statement (empty)
    Statement statement = conn.createStatement();
    statement.execute("CREATE TABLE user (uuid varchar(200) primary key, email varchar(200))");

  }

  static void _prepareStatement() throws SQLException {
    Connection conn = _new();

    // PreparedStatement (with query built)
    PreparedStatement preparedStatement = conn
        .prepareStatement("INSERT INTO user (uuid, email) values (?,?)");
    preparedStatement.setString(1, "000-000-000");
    preparedStatement.setString(2, "mail@mail.com");
  }
}
