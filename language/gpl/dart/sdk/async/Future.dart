import 'dart:async';

void main() {
  /**
   * Static
   */
  FutureValue();
  FutureDelayed();

  /**
   * Instance
   */
  FutureThen();
  FutureCatchError();
  FutureTimeout();
  FutureWhenComplete(); // finally
}

Future<String> FutureValue() {
  // Return value in the future (but right away)
  Future<String> task = Future.value('anything');

  return task;
}

void FutureDelayed() {
  // Return value in the future (after 1 s)
  Future<String> task = Future.delayed(Duration(seconds: 1), () {
    return "after 1s";
  });
}

void FutureThen() {
  Future<String> task = FutureValue();

  // perform an action when the value is available
  task.then((value) => print(value));
}

void FutureCatchError() {
  Future<String> task = FutureValue();

  task.catchError(
    // function to handle the exception
    (e) {
      print(e);
    },

    // test if it's a valid exception
    test: (e) => e is TimeoutException,
  ).catchError(
    // catch Errors can be chained (the first one to match is the handler)
    (e) {
      print(e);
    },
    test: (e) => e is Exception,
  );
}

void FutureTimeout() {
  Future<String> task = FutureValue();

  task.timeout(Duration(seconds: 5));
}

void FutureWhenComplete() {
  Future<String> task = Future.value('hello');

  // register a function to be executed when the future is complete
  // whether with a value or an error
  task.whenComplete(() => null);
}
