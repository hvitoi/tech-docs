import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

class MyServlet extends HttpServlet {

  @Override
  protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
    // getStatus()
    resp.setStatus(HttpServletResponse.SC_OK);

    // getWriter()
    resp.getWriter().println("I am a GET endpoint");
  }
}
