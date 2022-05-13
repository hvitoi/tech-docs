import org.eclipse.jetty.server.Handler;
import org.eclipse.jetty.server.Server;
import org.eclipse.jetty.servlet.ServletContextHandler;

class Main {
  public static void main(String[] args) throws Exception {
    /**
     * Static
     */
    ServerNew.run();

    /**
     * Instance
     */
    ServerStart.run();
    ServerJoin.run();
    ServerSetHandler.run();

  }
}

class ServerNew {
  static Server run() {
    // HTTP server configuration
    Server server = new Server(8080);
    return server;
  }
}

class ServerStart {
  static void run() throws Exception {
    Server server = ServerNew.run();

    // start the HTTP server
    server.start();
  }
}

class ServerJoin {
  static void run() throws InterruptedException {
    Server server = ServerNew.run();

    // keep the server up after starting it
    server.join();
  }
}

class ServerSetHandler {
  static void run() {
    Server server = ServerNew.run();

    // define a HTTP handler
    ServletContextHandler handler = new ServletContextHandler();
    handler.setContextPath("/");

    // handle a HTTP request\
    server.setHandler(handler);
  }
}