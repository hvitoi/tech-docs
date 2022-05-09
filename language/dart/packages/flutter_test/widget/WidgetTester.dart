import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';

void main() {
  testWidgets('do something', (WidgetTester tester) async {
    /**
     * load widget tree
     */
    await tester.pumpWidget(
      const MaterialApp(home: Text('hello')),
    );

    /**
     * Tap on a widget
     * Usually you want to pump() in order to wait everything to be processed
     */
    Finder widget1 = find.byType(Text);
    await tester.tap(widget1);

    /**
     * Kinda like a "wait". Jumps some frames in time
     * Executes the next micro task
     * After that you can verify for example if contact was saved
     */
    await tester.pump();

    /**
     * Similar to pump but execute as many tasks as necessary to settle down
     * It's composed of many pump calls
     * It will time out if some external call task is not mocked
     */
    await tester.pumpAndSettle();

    /**
     * Enter a text into a widget
     */
    Finder widget2 = find.byType(TextField);
    await tester.enterText(widget2, 'henry');
  });
}
