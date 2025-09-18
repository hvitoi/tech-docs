import java.lang.reflect.Field;

class Main {
  public static void main(String[] args) {
    ClassGetDeclaredFields.run();
    ClassGetDeclaredField.run();
    ClassGetFields.run();
    ClassGetField.run();

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
    Person person = new Person();
    Field field = person.getClass().getDeclaredFields()[0];

    String fieldName = field.getName();
  }

  static void _getType() {
    Person person = new Person();
    Field field = person.getClass().getDeclaredFields()[0];

    Class fieldType = field.getType();
  }

  static void _setAccessible() {
    Person person = new Person();
    Field field = person.getClass().getDeclaredFields()[0];

    field.setAccessible(true);
  }

  static void _canAccess() {
    Person person = new Person();
    Field field = person.getClass().getDeclaredFields()[0];

    field.canAccess(person); // false
    field.setAccessible(true);
    field.canAccess(person); // true
  }

  static void _set() {
    Person person = new Person("henry");
    Field field = person.getClass().getDeclaredFields()[0];

    field.setAccessible(true);

    try {
      field.set(person, "john"); // modify its value
    } catch (IllegalAccessException e) {
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
    }
  }

  static void _getBoolean() {
    Person person = new Person("henry");
    Field field = person.getClass().getDeclaredFields()[2]; // isHappy field

    field.setAccessible(true);

    try {
      boolean isHappy = field.getBoolean(person); // get boolean value from a field
    } catch (IllegalAccessException e) {
    }

  }
}

class ClassGetDeclaredFields {
  static void run() {
    Person person = new Person();
    Field[] fields = person.getClass().getDeclaredFields();
  }
}

class ClassGetDeclaredField {
  static void run() {
    Person person = new Person();

    try {
      Field field = person.getClass().getDeclaredField("name");
    } catch (NoSuchFieldException e) {
    }
  }
}

class ClassGetFields {
  static void run() {
    Person person = new Person();
    Field[] fields = person.getClass().getFields();
    // return only the public fields in both the class and all superclasses
  }
}

class ClassGetField {
  static void run() {
    Person person = new Person();

    try {
      Field field = person.getClass().getField("name");
    } catch (NoSuchFieldException e) {
    }
  }
}

class Person {
  private String name;
  private int age;
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
