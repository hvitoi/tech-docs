import 'package:flutter_test/flutter_test.dart';

void main() {
  test('do something', () {
    // throws error due to assert validations in the constructor
    var createObject = () => Object();
    expect(createObject, throwsAssertionError);
  });
}
