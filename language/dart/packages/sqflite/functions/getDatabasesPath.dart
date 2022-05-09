import 'package:sqflite/sqflite.dart';

/**
 * Get the path where sqlite databases are saved
 */

void main() async {
  String path = await getDatabasesPath();
}
