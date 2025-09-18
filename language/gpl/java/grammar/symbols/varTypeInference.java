import java.util.ArrayList;
import java.util.List;

class Main {
  public static void main(String[] args) {
    // compiler infers type
    // Works only for local variables, not fields or method parameters
    var list = new ArrayList<String>();

    // you still need to define is manually if you want to program to the interface
    List<String> list2 = new ArrayList<String>();
  }
}
