void main() {
  /**
   * Static
   */
  DateTimeNew();
  DateTimeNewNow();

  /**
   * Instance
   */
  DateTimeDay(); // property
  DateTimeSubtract();
  DateTimeIsAfter();
}

void DateTimeNew() {
  DateTime date = DateTime(2019); // 01/01/2019
}

DateTime DateTimeNewNow() {
  DateTime date = DateTime.now();
  return date;
}

void DateTimeDay() {
  DateTime date = DateTimeNewNow();

  // extract the day number
  int theDay = date.day;
}

void DateTimeSubtract() {
  DateTime date = DateTimeNewNow();

  DateTime subtractedDate = date.subtract(Duration(days: 1)); // yesterday
}

void DateTimeIsAfter() {
  DateTime date = DateTimeNewNow();
  DateTime otherDate = DateTimeNewNow();

  // verify if a date is after another date
  bool isAfter = date.isAfter(otherDate);
}
