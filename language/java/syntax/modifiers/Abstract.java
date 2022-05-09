// abstract class
// instances cannot be directly created from this class
abstract class Person {
  int name; // attributes created here are not abstract

  // abstract method
  // abstract methods are usefull when you must have a placeholder method name
  // here in order to set the object type as the super type. When objects have the
  // super type, they can only invoke methods that are described in the super
  // class (even though the implementation is pick from the child class)
  abstract void sayHello(); // if there is abstract method, the class must also be abstract

}
