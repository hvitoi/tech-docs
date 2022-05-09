package com.hvitoi;

import java.io.IOException;
import java.io.PrintWriter;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import java.sql.*;

@WebServlet("/TestDbServlet")
public class TestDbServlet extends HttpServlet {
  private static final long serialVersionUID = 1L;

  protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
    // setup connection variables
    String user = "root";
    String pass = "123";
    String jdbcUrl = "jdbc:mysql://localhost:3306/web_customer_tracker?allowPublicKeyRetrieval=true&useSSL=false";
    String driver = "com.mysql.cj.jdbc.Driver";

    try {
      // get writer
      PrintWriter out = response.getWriter();
      out.println("Connecting to database: " + jdbcUrl);

      // get connection
      Class.forName(driver); // load database driver
      Connection conn = DriverManager.getConnection(jdbcUrl, user, pass);
      out.println("Successfully connected to the database!");

      // close connection
      conn.close();

    } catch (Exception e) {
      e.printStackTrace();
      throw new ServletException(e);
    }

  }

}
