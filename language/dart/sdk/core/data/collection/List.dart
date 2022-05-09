void main() {
  /**
   * Static
   */
  ListDefault();
  ListGenerate();
  ListEmpty();

  /**
   * Instance
   */
  ListElementAt();
  ListAdd();
  ListRemove();
  ListRemoveWhere();
  ListMap();
  ListWhere(); // filter
  ListFold(); // reduce
  ListLength(); // property
  ListReversed(); // property
}

List<String> ListDefault() {
  List<String> list1 = <String>['hey', 'What\'s up?', 'Fine, thanks'];
  list1[0]; // first index

  /**
   * type inference
   */
  var mixedList = [
    'hey',
    23,
    [1, 2],
    'a'
  ];

  return list1;
}

void ListGenerate() {
  List<int> list = List.generate(5, (index) => index); // [0, 1, 2, 3, 4]
}

void ListEmpty() {
  List list = List.empty(growable: true);
}

void ListElementAt() {
  List<String> messages = ListDefault();

  // elementAt
  String el = messages.elementAt(0); // first index
}

void ListAdd() {
  List<String> messages = ListDefault();

  // add
  messages.add('Chris'); // return void
}

void ListRemove() {
  List<String> messages = ListDefault();

  // remove
  bool isRemoved = messages.remove('Chris');
}

void ListRemoveWhere() {
  List<String> messages = ListDefault();

  // remove where is condition is met
  messages.removeWhere((el) => el == 'Chris');
}

void ListMap() {
  List<String> messages = ListDefault();

  // map
  Iterable<String> iterable = messages.map((e) => e);
}

void ListWhere() {
  List<String> list = ListDefault();

  // filter elements that return true
  list.where((el) {
    return el == 'Chris';
  });
}

void ListFold() {
  List<int> list = [1, 2, 3];

  // filter elements that return true
  int totalSum = list.fold(0, (sum, el) => sum + el);
}

void ListLength() {
  List<String> messages = ListDefault();

  // list size
  int size = messages.length;
}

void ListReversed() {
  List<String> list = ListDefault();

  // reverse the list
  Iterable<String> reversed = list.reversed;
}
