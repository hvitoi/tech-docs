import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';

/**
 * Open a database from a file
 */

void main() async {
  String path = await getDatabasesPath();
  String dbPath = join(path, 'mydatabase.db');

  Future<Database> database = openDatabase(
    path,
    version: 1,
    onCreate: (db, version) {
      db.execute('CREATE TABLE contacts('
          'id INTEGER PRIMARY KEY, '
          'name TEXT, '
          'account_number INTEGER)');
    },
    onDowngrade: onDatabaseDowngradeDelete, // delete db on downgrading version
  );
}
