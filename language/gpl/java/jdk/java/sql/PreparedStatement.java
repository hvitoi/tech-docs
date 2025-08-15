import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

class Main {
  public static void main(String[] args) throws SQLException {
    /**
     * Static
     */
    _new();

    /**
     * Instance
     */
    _setString();
    _execute();
    _executeQuery();
  }

  static PreparedStatement _new() throws SQLException {
    Connection conn = DriverManager.getConnection("jdbc:sqlite:user_database.db");
    PreparedStatement preparedStatement = conn
        .prepareStatement("INSERT INTO user (uuid, email) values (?,?)");
    return preparedStatement;
  }

  static void _setString() throws SQLException {
    PreparedStatement ps = PreparedStatementNew.run();

    // Set the parameters for a query
    ps.setString(1, "000-000-000");
    ps.setString(2, "mail@mail.com");

    // It must be executed after setting the parameters
  }

  static void _execute() throws SQLException {
    PreparedStatement ps = PreparedStatementNew.run();

    ps.execute();
  }

  static void _executeQuery() throws SQLException {
    PreparedStatement ps = PreparedStatementNew.run();

    // same as execute(), but returns the resultSet
    ResultSet resultSet = ps.executeQuery();
  }
}
