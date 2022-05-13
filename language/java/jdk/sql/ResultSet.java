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
    ResultSetNew.run();

    /**
     * Instance
     */
    ResultSetNext.run();

  }
}

class ResultSetNew {
  static ResultSet run() throws SQLException {
    Connection conn = DriverManager.getConnection("jdbc:sqlite:user_database.db");
    PreparedStatement preparedStatement = conn
        .prepareStatement("INSERT INTO user (uuid, email) values (?,?)");
    ResultSet resultSet = preparedStatement.executeQuery();
    return resultSet;
  }
}

class ResultSetNext {
  static void run() throws SQLException {
    ResultSet rs = ResultSetNew.run();

    // goes to the next line in the result set
    boolean goneToNextLine = rs.next();
  }
}
