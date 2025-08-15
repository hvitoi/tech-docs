import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  testWidgets('do something', (WidgetTester tester) async {
    await tester.pumpWidget(const MaterialApp(home: Text('hello')));

    /**
     * byType
     */
    Finder w1 = find.byType(Text);

    /**
     * widgetWithIcon
     */
    Finder w2 = find.widgetWithIcon(IconButton, Icons.monetization_on);

    /**
     * widgetWithText
     */
    Finder w3 = find.widgetWithText(IconButton, 'hello');

    /**
     * text
     */
    Finder w4 = find.text('hello');

    /**
     * byWidgetPredicate
     */
    Finder w5 = find.byWidgetPredicate((Widget widget) {
      return (widget is Text);
    });

    /**
     * byKey
     */
    Finder w6 = find.byKey(Key('myDialog'));
  });
}
