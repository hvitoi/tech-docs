import 'dart:async';

void main() {
  /**
   * Static
   */
  ExceptionNew();

  /**
   * Instance
   */
  ExceptionMessage();
}

void ExceptionNew() {
  throw Exception("Error while fetching");
}

void ExceptionMessage() {
  TimeoutException e = TimeoutException("Error while fetching");
  e.message;
}
