void main() {
  var awesomePerson = Human("I am ...", name: "Henry", message: "Be good");
}

class Human {
  /**
   * Properties
   */
  final String name; // can't be changed
  String gender = "male"; // default value
  String? message; // optional
  String _secret; // private (accessible only within the class)
  String get fullName {
    // getter: mix of method and property
    // it never receives any argument
    return this.name + "Silva";
  }

  /**
   * Constructors
   */

  // Unnamed constructor
  Human(
    // Positional parameters
    this._secret, // private only be positional

    // Named parameters
    {
    required this.name,
    this.message,
  });

  // Invoke super
  Human.secondConstructor(
    this._secret, {
    required this.name,
    this.message,
  })  : assert(name.length > 0),
        super(); // super constructor must be the last to be called
  Human.thirdConstructor(
    this._secret, {
    required this.name,
    this.message,
  }) {
    // super();
    assert(name.length > 0);
    assert(_secret.length > 0);
  }

  /**
   * Methods
   */
  void _sayHello = () {
    // private method (accessible within the class)
    print('hello');
  };
}

// private class (accessible within the library)
class _Person extends Human {
  _Person(String secret, {required String name}) : super(secret, name: name);

  /**
   * const constructor can't have body
   */
  // const Person({String? myMessage}) : super(message: myMessage);

  /**
   * Named constructor
   */

  // automatically saves the input into the class properties
  // Person.myPositionalParametersShortSyntax(this.name, this.age);

  // // required parameters must be marked as required
  // // optional parameters must have a default value
  // Person.myNamedParamaters({required String name, int age = 0}) {
  //   this.name = name;
  //   this.age = age;
  // }
  // Person.myNamedParametersShortSyntax({this.name = "lol", this.age = 0});

  // Person.myNamedAndPositionalParameters(this.name, {this.age = 0});

}
