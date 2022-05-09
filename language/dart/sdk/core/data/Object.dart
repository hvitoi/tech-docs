void main() {
  ObjectNew();
}

void ObjectNew() {
  Object a = "hello";
  Object b = 1;
  Object c = MyObject("henry", 10);
}

class MyObject extends Object {
  String name;
  int age;

  MyObject(this.name, this.age);

  /**
   * == operator
   */

  // defines the criteria of equality for objects of this class

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is MyObject &&
          runtimeType == other.runtimeType &&
          name == other.name &&
          age == other.age;

  /**
   * Hashcode
   */
  @override
  int get hashCode => name.hashCode ^ age.hashCode;
}
