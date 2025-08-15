void main() {
  Future<String> task = Future.value("a");

  task.catchError(
    // function to handle the exception
    (e) {
      print(e);
    },

    // test if it's a valid exception
    test: (e) => e is Exception,
  );

  if ("aaa" is String) {
    print("it's a strng");
  }
}
