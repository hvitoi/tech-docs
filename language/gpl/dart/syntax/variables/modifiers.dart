void main() {
  /**
   * Type inference
   */
  var myVar = "hello"; // variable
  const myConst = "hello"; // constant at compile-time & runtime
  final myFinal = "hello"; // constant at runtime only

  /**
   * Type explicit
   */
  String myVar2 = "hello";
  const String myConst2 = "hello";
  final String myFinal2 = "hello";

  /**
   * Optional variable
   */
  String? iAmOptional = 'hello';
  iAmOptional = null; // ok

  /**
   * Address & Value
   */
  var a = const ["hello"]; // variable address, constant value
  a.add("hey"); // fail!
  a = ["hey"]; // address is changed, but old value is maintained

  const b = ["hello"]; // constant address, constant value
  const b2 = const ["hello"]; // same
  b.add("hey"); // fail!

  var c = ["hello"]; // variable address, variable value
  c.add("hey"); // ok
}
