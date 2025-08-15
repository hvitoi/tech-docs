import 'package:path/path.dart';
import 'package:sqflite/sqflite.dart';

void main() {
  /**
   * Instance
   */
  DatabaseInsert();
  DatabaseQuery();
}

Future<Database> getMyDatabase() async {
  String path = await getDatabasesPath();
  String dbPath = join(path, 'mydatabase.db');

  return openDatabase(
    path,
    version: 1,
    onCreate: (db, version) {
      db.execute('CREATE TABLE contacts('
          'id INTEGER PRIMARY KEY, '
          'name TEXT, '
          'account_number INTERGER)');
    },
  );
}

void DatabaseInsert() async {
  Database db = await getMyDatabase();

  Map<String, dynamic> contactData = {
    'id': 0, // if id is not provided, SQLite will automatically add it
    'name': 'Henry',
    'account_number': 0001
  };
  db.insert('contacts', contactData);
}

void DatabaseQuery() async {
  Database db = await getMyDatabase();

  // Result is a list of maps
  List<Map<String, dynamic>> records = await db.query('contacts');
}
