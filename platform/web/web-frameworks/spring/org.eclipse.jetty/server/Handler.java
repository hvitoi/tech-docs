import org.eclipse.jetty.server.Handler;
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
    // this handler is usually added to the setHandler of the HTTP Server
    Handler handler = new ServletContextHandler();
    return handler;
  }
}
