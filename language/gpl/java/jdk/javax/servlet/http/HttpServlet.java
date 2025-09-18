import java.io.IOException;

import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

// It's a server-side HTTP API
// Handle incoming HTTP requests

class MyServlet extends HttpServlet {

  @Override
  public void init(ServletConfig config) throws ServletException {
    // executes when the servlet is created
    super.init(config);

  }

  @Override
  public void destroy() {
    // executes when the servlet is destroyed
    super.destroy();
  }

  @Override
  protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
    resp.setStatus(HttpServletResponse.SC_OK);
    resp.getWriter().println("I am a GET endpoint");
  }

  @Override
  protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
    resp.setStatus(HttpServletResponse.SC_OK);
    resp.getWriter().println("I am a POST endpoint");
  }

}
