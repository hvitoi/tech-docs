import org.eclipse.jetty.servlet.ServletContextHandler;
import org.eclipse.jetty.servlet.ServletHolder;
import org.eclipse.jetty.server.Server;

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
    ServletContextHandler servletContextHandler = new ServletContextHandler();
    return servletContextHandler;
  }
}

class ServletContextHandlerSetContextPath {
  static void run() {
    ServletContextHandler sch = ServletContextHandlerNew.run();

    // the context path is the root path
    sch.setContextPath("/");
  }
}

class ServletContextHandlerAddServlet {
  static void run() {
    ServletContextHandler sch = ServletContextHandlerNew.run();
    ServletHolder servletHolder = new ServletHolder();

    // add an endpoint (a servlet), servlet contains the logic the handle a request
    sch.addServlet(servletHolder, "/new");
  }
}
