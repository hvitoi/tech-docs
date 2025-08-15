import 'package:flutter/material.dart';

class Result extends StatelessWidget {
  final int totalScore;
  final VoidCallback resetHandler;

  Result(this.totalScore, this.resetHandler);

  String get phrase {
    String resultText;
    if (totalScore <= 8) {
      resultText = 'You are awesome';
    } else if (totalScore <= 12) {
      resultText = 'You are great';
    } else {
      resultText = 'You are meh';
    }
    return resultText;
  }

  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        children: [
          Text(
            phrase,
            style: TextStyle(fontSize: 36, fontWeight: FontWeight.bold),
            textAlign: TextAlign.center,
          ),
          TextButton(
            child: Text('Restart Quiz!'),
            style: TextButton.styleFrom(primary: Colors.orange),
            onPressed: resetHandler,
          )
        ],
      ),
    );
  }
}
