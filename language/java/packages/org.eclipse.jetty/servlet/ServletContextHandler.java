import org.eclipse.jetty.server.ServletContextHandler;
import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.servlet.ServletContextServletContextHandler;

class Main {
  public static void main(String[] args) {
    /**
     * Static
     */
    ServletContextHandlerNew.run();

    /**
     * Instance
     */
    ServletContextHandlerSetContextPath.run();
    ServletContextHandlerAddServlet.run();

  }
}

class ServletContextHandlerNew {
  static ServletContextHandler run() {
    Server server = new Server(8080);
    ServletContextHandler servletContextHandler = new ServletContextServletContextHandler();
    return servletContextHandler;
  }
}

class ServletContextHandlerSetContextPath {
  static void run() {
    org.eclipse.jetty.servlet.ServletContextHandler sch = ServletContextHandlerNew.run();

    // the endpoint to handle
    sch.setContextPath("/");
  }
}

class ServletContextHandlerAddServlet {
  static void run() {
    org.eclipse.jetty.servlet.ServletContextHandler sch = ServletContextHandlerNew.run();

    // the endpoint to handle
    sch.addServlet(servlet, pathSpec);
  }
}
