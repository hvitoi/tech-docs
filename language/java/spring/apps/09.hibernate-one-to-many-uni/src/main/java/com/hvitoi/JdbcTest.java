package com.hvitoi;

import java.sql.Connection;
import java.sql.DriverManager;

public class JdbcTest {
    public static void main(String[] args) {
        String jdbcUrl = "jdbc:mysql://localhost:3306/hb-one-to-many-uni";
        String user = "root";
        String pass = "123";

        try {
            System.out.println("Connecting to DB: " + jdbcUrl);
            Connection conn = DriverManager.getConnection(jdbcUrl, user, pass);
            System.out.println("Connection successful: " + conn);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
