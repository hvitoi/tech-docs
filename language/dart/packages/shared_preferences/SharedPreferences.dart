import 'package:shared_preferences/shared_preferences.dart';

void main() async {
  // Instance
  final prefs = await SharedPreferences.getInstance();

  /**
   * Write
   */
  await prefs.setInt('counter', 10);
  await prefs.setBool('repeat', true);
  await prefs.setDouble('decimal', 1.5);
  await prefs.setString('action', 'Start');
  await prefs.setStringList('items', <String>['Earth', 'Moon', 'Sun']);

  /**
   * Read
   */
  final int? counter = prefs.getInt('counter');
  final bool? repeat = prefs.getBool('repeat');
  final double? decimal = prefs.getDouble('decimal');
  final String? action = prefs.getString('action');
  final List<String>? items = prefs.getStringList('items');

  /**
   * Delete
   */
  final success = await prefs.remove('counter');

  /**
   * Testing
   */
  Map<String, Object> values = <String, Object>{'counter': 1};
  SharedPreferences.setMockInitialValues(values);
}
