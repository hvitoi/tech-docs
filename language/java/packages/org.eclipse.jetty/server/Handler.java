import org.eclipse.jetty.server.Handler;
import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.servlet.ServletContextHandler;

class Main {
  public static void main(String[] args) {
    /**
     * Static
     */
    HandlerNew.run();

  }
}

class HandlerNew {
  static Handler run() {
    Server server = new Server(8080);
    Handler handler = new ServletContextHandler();
    return handler;
  }
}
