import 'package:localstorage/localstorage.dart';

void main() {
  /**
   * Static
   */
  LocalStorageNew();

  /**
   * Instance
   */
  LocalStorageReady();
  LocalStorageGetItem();
  LocalStorageSetItem();
}

void LocalStorageNew() {
  final LocalStorage storage = LocalStorage('myfile.json');
}

void LocalStorageReady() {
  final LocalStorage storage = LocalStorage('myfile.json');

  Future<bool> isReady = storage.ready;
  storage.ready.then((isReady) {
    if (isReady) {
      storage.getItem('key');
    }
  });
}

void LocalStorageGetItem() async {
  final LocalStorage storage = LocalStorage('myfile.json');
  await storage.ready;

  storage.getItem('key');
}

void LocalStorageSetItem() async {
  final LocalStorage storage = LocalStorage('myfile.json');
  await storage.ready;

  storage.setItem('key', 'value');
}
