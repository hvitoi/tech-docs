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
    ConnectionNew.run();

    /**
     * Instance
     */
    ConnectionCreateStatement.run();
    ConnectionPrepareStatement.run();

  }
}

class ConnectionNew {
  static Connection run() throws SQLException {
    Connection conn = DriverManager.getConnection("jdbc:sqlite:user_database.db");
    return conn;
  }
}

class ConnectionCreateStatement {
  static void run() throws SQLException {
    Connection conn = ConnectionNew.run();

    // Statement (empty)
    Statement statement = conn.createStatement();
    statement.execute("CREATE TABLE user (uuid varchar(200) primary key, email varchar(200))");

  }
}

class ConnectionPrepareStatement {
  static void run() throws SQLException {
    Connection conn = ConnectionNew.run();

    // PreparedStatement (with query built)
    PreparedStatement preparedStatement = conn
        .prepareStatement("INSERT INTO user (uuid, email) values (?,?)");
    preparedStatement.setString(1, "000-000-000");
    preparedStatement.setString(2, "mail@mail.com");
  }
}