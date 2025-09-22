import java.lang.reflect.Modifier;

class Main {
  public static void main(String[] args) {
    // Static methods
    _isAbstract();
    _isPublic();
  }

  static void _isAbstract() {
    int modifier = Person.class.getModifiers();
    boolean isAbstract = Modifier.isAbstract(modifier); // false
  }

  static void _isPublic() {
    int modifier = Person.class.getModifiers();
    boolean isPublic = Modifier.isPublic(modifier); // false
  }
}

class Person {
}
