import 'package:flutter/material.dart';
import 'package:intl/intl.dart';

class NewTransaction extends StatefulWidget {
  final Function newTx;

  const NewTransaction(this.newTx, {Key? key}) : super(key: key);

  @override
  State<NewTransaction> createState() => _NewTransactionState();
}

class _NewTransactionState extends State<NewTransaction> {
  // assign a controller to TextField (listens and saves user input)
  final _titleController = TextEditingController();
  final _amountController = TextEditingController();
  DateTime? _selectedDate;

  void _submitData() {
    final enteredTitle = _titleController.text;
    final enteredAmount = double.parse(_amountController.text);

    if (enteredTitle.isEmpty && enteredAmount <= 0 || _selectedDate == null) {
      return;
    }

    // "widget": reference to the StatefulWidget
    widget.newTx(enteredTitle, enteredAmount, _selectedDate);

    // "context": reference to the context
    // Close the top most screen/widget
    Navigator.of(context).pop();
  }

  void _presentDatePicker() {
    showDatePicker(
      context: context,
      initialDate: DateTime.now(),
      firstDate: DateTime(2019),
      lastDate: DateTime.now(),
    ).then((pickedDate) {
      setState(() {
        _selectedDate = pickedDate;
      });
    });
  }

  @override
  Widget build(BuildContext context) {
    return Card(
      child: Container(
        padding: const EdgeInsets.all(10),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.end,
          children: <Widget>[
            TextField(
              decoration: const InputDecoration(labelText: 'Title'),
              controller: _titleController,
            ),
            TextField(
              decoration: const InputDecoration(labelText: 'Amount'),
              controller: _amountController,
              keyboardType: TextInputType.number,
              onSubmitted: (_) => _submitData(), // For the keyboard "enter"
            ),
            Row(
              children: [
                Expanded(
                  child: Text(_selectedDate == null
                      ? 'No Date Chosen!'
                      : DateFormat.yMd().format(_selectedDate!)),
                ),
                TextButton(
                  onPressed: _presentDatePicker,
                  child: const Text('Choose date'),
                  style: const ButtonStyle(),
                ),
              ],
            ),
            ElevatedButton(
              child: const Text('Add Transaction'),
              onPressed: _submitData,
              style: const ButtonStyle(),
            )
          ],
        ),
      ),
    );
  }
}
