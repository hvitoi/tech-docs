import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  testWidgets('do something', (WidgetTester tester) async {
    await tester.pumpWidget(const MaterialApp(home: Text('hello')));

    Finder textWidget = find.byType(Text);
  });
}
