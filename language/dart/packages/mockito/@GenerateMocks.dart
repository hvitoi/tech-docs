import 'package:mockito/annotations.dart';
import 'package:mockito/mockito.dart';
import 'mock/cat.dart';
import 'mock/cat.mocks.dart';

// Annotation which generates the cat.mocks.dart library and the MockCat class.
@GenerateMocks([Cat])
void main() {
  // Create mock object.
  // In order to generate it you must run build_runner
  // dart run build_runner build
  var cat = MockCat();

  // Interact with the mock object.
  cat.sound();
}
