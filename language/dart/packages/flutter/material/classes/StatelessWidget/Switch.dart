import 'package:flutter/material.dart';

/**
 * Toggle on/off something 
 */

Widget main() {
  return Switch(
    value: true,
    onChanged: (val) {
      // setState(() {
      // _isChartVisible = val;
      // });
    },
  );
}
