void main() {
  /**
   * Static 
   */
  FunctionNew();

  /**
   * Instance
   */
  FunctionCall();
}

void FunctionNew() {
  /**
   * Dynamic parameters & return value
   */
  Function fn1 = (num1, num2) {
    return num1 + num2;
  };

  /**
   * Static parameters & return value
   */
  int Function(int, int) fn2 = (int num1, int num2) {
    return num1 + num2;
  };

  /**
   * Named parameters (optional if not marked with required)
   */
  Function fn3 = ({
    num1, // optional (dynamic)
    int? num2, // optional (explicit)
    required num3, // required (dynamic)
    required int num4, // requzired (explicit)
  }) {
    return num1 + num2 + num3 + num4;
  };

  /**
   * anonymous function
   */
  Function fn4 = () => print("I am an annonymous function");
}

void FunctionCall() {
  Function fn = (num1, num2) => num1 + num2;
  fn.call(1, 2);
}
