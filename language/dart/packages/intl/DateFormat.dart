import 'package:intl/intl.dart';

void main() {
  /**
   * Static methods
   */
  DateFormatNew();
  DateFormatNewE();
  DateFormatNewYMMMMd();

  /**
   * Instance methods
   */
  DateFormatFormat();
}

DateFormat DateFormatNew() {
  DateFormat formatter1 = DateFormat();
  DateFormat formatter2 = DateFormat('yyyy-MM-dd');
  return formatter1;
}

void DateFormatNewE() {
  DateFormat formatter = DateFormat.E(); // weekday letter
}

void DateFormatNewYMMMMd() {
  DateFormat formatter = DateFormat.yMMMMd();
}

void DateFormatFormat() {
  DateFormat formatter = DateFormatNew();
  DateTime date = DateTime.now();

  // convert to string
  String formattedDate = formatter.format(date);
}
