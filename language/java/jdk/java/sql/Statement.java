import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;
import java.sql.Statement;

class Main {
  public static void main(String[] args) throws SQLException {
    /**
     * Static
     */
    StatementNew.run();

    /**
     * Instance
     */
    StatementExecute.run();

  }
}

class StatementNew {
  static Statement run() throws SQLException {
    Connection conn = DriverManager.getConnection("jdbc:sqlite:user_database.db");
    Statement statement = conn.createStatement();
    return statement;
  }
}

class StatementExecute {
  static void run() throws SQLException {
    Statement statement = StatementNew.run();
    statement.execute("CREATE TABLE user (uuid varchar(200) primary key, email varchar(200))");
  }
}
