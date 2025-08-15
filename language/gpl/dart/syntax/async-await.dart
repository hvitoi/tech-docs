void main() async {
  Future<String> task = Future.delayed(Duration(seconds: 1), () {
    return "after 1s";
  });

  String res = await task;
}
