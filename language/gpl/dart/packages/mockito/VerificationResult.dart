import 'package:mockito/mockito.dart';
import 'mock/cat.mocks.dart';

void main() {
  var cat = MockCat();
  cat.sound();

  VerificationResult verification = verify(cat.sound());

  /**
   * Verify if a method was called n times
   */
  verification.called(1);
}
