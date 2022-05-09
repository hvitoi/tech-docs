void main() {
  try {
    throw Exception();
  } catch (e) {
    print(e);
  } finally {
    print('Done.');
  }
}
