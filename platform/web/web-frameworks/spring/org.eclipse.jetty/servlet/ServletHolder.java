import org.eclipse.jetty.servlet.ServletHolder;

class Main {
  public static void main(String[] args) {
    /**
     * Static
     */
    ServletHolderNew.run();

  }
}

class ServletHolderNew {
  static ServletHolder run() {
    // holds an empty servlet
    ServletHolder servletHolder = new ServletHolder();
    return servletHolder;
  }
}
