import java.lang.reflect.Constructor;
import java.lang.reflect.Field;
import java.lang.reflect.Method;
import java.util.stream.Stream;

class Main {
  public static void main(String[] args) {
    // Static methods
    _forName();

    // Instance methods
    _isInstance(); // -> boolean
    _getName(); // -> String
    _getCanonicalName(); // -> String
    _getSimpleName(); // -> String

    _getModifiers(); // -> Integer
    _getSuperclass(); // -> Class
    _getInterfaces(); // -> Class[]

    _getPackage(); // -> Package

    _getConstructors(); // -> Constructor[]
    _getConstructor(); // -> Constructor

    _getDeclaredFields(); // -> Field[]
    _getDeclaredField(); // -> Field
    _getFields(); // -> Field[]
    _getField(); // -> Field

    _getDeclaredMethods(); // -> Method[]
    _getDeclaredMethod(); // -> Method
    _getMethods(); // -> Method[]
    _getMethod(); // -> Method
  }

  static void _forName() {
    // returns the class associated with a given name
    // the type <?> is unknown because it's only known at runtime
    try {
      Class<?> clazz = Class.forName("java.lang.String");
      var clazz2 = Class.forName("java.lang.String");
    } catch (ClassNotFoundException e) {
      e.printStackTrace();
    }

    // Usually the class is get using Object.getClass()
  }

  static void _isInstance() {
    var clazz = String.class;
    boolean a = clazz.isInstance("hey");
    System.out.println(a);
  }

  static void _getName() {
    var clazz = "hello".getClass();
    var clazz2 = String.class.getClass();
    String name = clazz.getName(); // java.lang.String (DQN)
  }

  static void _getCanonicalName() {
    var clazz = "hello".getClass();
    String canonicalName = clazz.getCanonicalName(); // java.lang.String
  }

  static void _getSimpleName() {
    var clazz = "hello".getClass();
    String simpleName = clazz.getSimpleName(); // String
  }

  static void _getPackage() {
    var clazz = "hello".getClass();
    Package classPackage = clazz.getPackage(); // java.lang
  }

  static void _getSuperclass() {
    var clazz = "hello".getClass();
    Class<?> superClass = clazz.getSuperclass(); // java.lang.Object
  }

  static void _getInterfaces() {
    // Get interfaces that a class explicitly declares as implemented
    var clazz = "hello".getClass();
    Class<?>[] classInterfaces = clazz.getInterfaces(); // list containing interface Printable
  }

  static void _getModifiers() {
    var clazz = "hello".getClass();
    int modifiers = clazz.getModifiers(); // 1
  }

  static void _getConstructors() {
    var clazz = "hello".getClass();
    Constructor<?>[] constructors = clazz.getConstructors();
  }

  static void _getConstructor() {
    var clazz = "hello".getClass();
    try {
      // get the constructor with no args
      Constructor<?> constructor = clazz.getConstructor();
      // get the constructor with 1 arg (a string)
      Constructor<?> constructor2 = clazz.getConstructor(String.class);
    } catch (NoSuchMethodException | SecurityException e) {
      e.printStackTrace();
    }
  }

  static void _getDeclaredFields() {
    var clazz = "hello".getClass();
    Field[] fields = clazz.getDeclaredFields();

    Stream.of(fields).anyMatch(e -> e.getType() == Integer.class); // check if any of the fields is an integer

    // for (var f : fields) {
    // System.out.println(f);
    // }
  }

  static void _getDeclaredField() {
    var clazz = "hello".getClass();
    try {
      Field field = clazz.getDeclaredField("hash");
    } catch (NoSuchFieldException e) {
      e.printStackTrace();
    }
  }

  static void _getFields() {
    // return only the public fields in both the class and all superclasses
    var clazz = "hello".getClass();
    Field[] fields = clazz.getFields();
  }

  static void _getField() {
    // return a single public field by its name
    var clazz = "hello".getClass();
    try {
      Field field = clazz.getField("CASE_INSENSITIVE_ORDER");
    } catch (NoSuchFieldException e) {
      e.printStackTrace();
    }
  }

  static void _getDeclaredMethods() {
    var clazz = "hello".getClass();
    Method[] methods = clazz.getDeclaredMethods();

    // for (var m : methods) {
    // System.out.println(m);
    // }
  }

  static void _getDeclaredMethod() {
    var clazz = "hello".getClass();
    try {
      Method method = clazz.getDeclaredMethod("lastIndexOfNonWhitespace");
    } catch (NoSuchMethodException e) {
      e.printStackTrace();
    }
  }

  static void _getMethods() {
    // return only the public methods in both the class and all superclasses
    var clazz = "hello".getClass();
    Method[] methods = clazz.getMethods();
  }

  static void _getMethod() {
    // return a single public method by its name
    var clazz = "hello".getClass();
    try {
      Method method = clazz.getMethod("describeConstable");
    } catch (NoSuchMethodException e) {
      e.printStackTrace();
    }
  }

}
