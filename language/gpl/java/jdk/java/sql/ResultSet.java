import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;

class Main {
  public static void main(String[] args) throws SQLException {
    _new();

    // Instance methods
    _next();
  }

  static ResultSet _new() throws SQLException {
    Connection conn = DriverManager.getConnection("jdbc:sqlite:user_database.db");
    PreparedStatement preparedStatement = conn
        .prepareStatement("INSERT INTO user (uuid, email) values (?,?)");
    ResultSet resultSet = preparedStatement.executeQuery();
    return resultSet;
  }

  static void _next() throws SQLException {
    ResultSet rs = _new();

    // goes to the next line in the result set
    boolean goneToNextLine = rs.next();
  }
}
