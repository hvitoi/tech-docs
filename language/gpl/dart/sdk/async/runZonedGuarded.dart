import 'dart:async';

void main() {
  // Creates a new zone using [Zone.fork] then runs [body] in that zone and returns the result.
  runZonedGuarded(() => print("hello"), (e, s) => print(e));
}
