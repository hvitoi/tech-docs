import 'package:mockito/mockito.dart';
import 'mock/cat.mocks.dart';

void main() {
  var cat = MockCat();

  // Interact with the mock object.
  cat.sound();

  // Returns the result of the verification
  verify(cat.sound());
}
