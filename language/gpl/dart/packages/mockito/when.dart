import 'package:mockito/mockito.dart';
import 'mock/cat.mocks.dart';

void main() {
  var cat = MockCat();

  // modify a behavior of the mock before calling it
  when(cat.sound()).thenAnswer((realInvocation) {
    print('sound() was invoked. ${realInvocation.memberName}');
    return "meowww";
  });

  cat.sound();
}
