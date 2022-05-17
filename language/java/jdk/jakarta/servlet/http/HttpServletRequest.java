import java.io.IOException;

import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

class MyServlet extends HttpServlet {

  @Override
  protected void doGet(javax.servlet.http.HttpServletRequest req, HttpServletResponse resp)
      throws ServletException, IOException {

    // getParameter()
    req.getParameter("email"); // query parameter
  }

}
