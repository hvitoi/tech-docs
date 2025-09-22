import java.lang.reflect.Field;

class Main {
  public static void main(String[] args) {
    // Instance methods
    _getName();
    _getType();
    _setAccessible();
    _canAccess();
    _set();
    _get();
    _getBoolean();
  }

  static void _getName() {
    Field field = Person.class.getDeclaredFields()[0];
    String fieldName = field.getName();
  }

  static void _getType() {
    Field field = Person.class.getDeclaredFields()[0];
    Class<?> fieldType = field.getType();
  }

  static void _setAccessible() {
    Field field = Person.class.getDeclaredFields()[0];
    field.setAccessible(true);
  }

  static void _canAccess() {
    Person p = new Person();
    Field field = p.getClass().getDeclaredFields()[0];

    field.canAccess(p); // false
    field.setAccessible(true);
    field.canAccess(p); // true
  }

  static void _set() {
    Person p = new Person("henry");
    Field field = p.getClass().getDeclaredFields()[0];

    field.setAccessible(true);
    try {
      field.set(p, "john"); // modify its value
    } catch (IllegalAccessException e) {
      e.printStackTrace();
    }

  }

  static void _get() {
    Person person = new Person("henry");
    Field field = person.getClass().getDeclaredFields()[0];

    field.setAccessible(true);
    try {
      Object value = field.get(person);
      // Object value = field.get(null); // if field is public static
    } catch (IllegalAccessException e) {
      e.printStackTrace();
    }
  }

  static void _getBoolean() {
    Person person = new Person("henry");
    Field field = person.getClass().getDeclaredFields()[1]; // isHappy field

    field.setAccessible(true);
    try {
      boolean isHappy = field.getBoolean(person); // get boolean value from a field
    } catch (IllegalAccessException e) {
      e.printStackTrace();
    }

  }
}

class Person {
  private String name;
  private boolean isHappy;

  public Person() {
  }

  public Person(String name) {
    this.name = name;
  }

  public void printName() {
    System.out.println(this.name);
  }

}
