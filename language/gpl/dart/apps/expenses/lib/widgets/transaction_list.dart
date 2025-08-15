import 'package:flutter/material.dart';
import 'package:intl/intl.dart';
import 'package:personal_expenses/models/transaction.dart';

class TransactionList extends StatelessWidget {
  final List<Transaction>? transactions;
  final Function deleteTransaction;

  const TransactionList(this.transactions, this.deleteTransaction, {Key? key})
      : super(key: key);

  @override
  Widget build(BuildContext context) {
    return SizedBox(
      height: MediaQuery.of(context).size.height * 0.7, // 70% of the screen
      child: transactions!.isEmpty
          ? Column(
              children: <Widget>[
                Text(
                  "Nothing to display here",
                  style: Theme.of(context).textTheme.headline6,
                ),
                SizedBox(
                  height: 200,
                  child: Image.asset(
                    'assets/images/waiting.png',
                    fit: BoxFit.cover,
                  ),
                ),
              ],
            )
          : ListView.builder(
              itemCount: transactions!.length, // execute itemBuild n times
              itemBuilder: (ctx, i) => Card(
                margin: const EdgeInsets.symmetric(vertical: 8, horizontal: 5),
                elevation: 5,
                child: ListTile(
                  leading: CircleAvatar(
                    // usually an image
                    radius: 30,
                    child: Text('\$${transactions![i].amount}'),
                  ),
                  title: Text(
                    transactions![i].title,
                    style: Theme.of(context).textTheme.headline6,
                  ),
                  subtitle:
                      Text(DateFormat.yMMMd().format(transactions![i].date)),
                  trailing: IconButton(
                    icon: const Icon(Icons.delete),
                    color: Theme.of(context).errorColor,
                    onPressed: () => deleteTransaction(transactions![i].id),
                  ),
                  // child: Row(
                  //   children: <Widget>[
                  //     Container(
                  //       decoration: BoxDecoration(
                  //         border: Border.all(
                  //           color: Theme.of(context).primaryColor,
                  //           width: 2,
                  //         ),
                  //       ),
                  //       margin: const EdgeInsets.symmetric(
                  //         vertical: 10,
                  //         horizontal: 50,
                  //       ),
                  //       padding: const EdgeInsets.all(10),
                  //       child: Text(
                  //         '\$${transactions![i].amount.toStringAsFixed(2)}',
                  //         style: TextStyle(
                  //           fontWeight: FontWeight.bold,
                  //           fontSize: 20,
                  //           color: Theme.of(context).primaryColor,
                  //         ),
                  //       ),
                  //     ),
                  //     Column(
                  //       crossAxisAlignment: CrossAxisAlignment.start,
                  //       children: [
                  //         Text(
                  //           transactions![i].title,
                  //           style: Theme.of(context)
                  //               .textTheme
                  //               .headline6, // from global
                  //         ),
                  //         Text(
                  //           DateFormat.yMMMMd().format(transactions![i].date),
                  //           style: const TextStyle(
                  //             fontWeight: FontWeight.normal,
                  //             fontSize: 16,
                  //             color: Colors.grey,
                  //           ),
                  //         ),
                  //       ],
                  //     )
                  //   ],
                  // ),
                ),
              ),
            ),
    );
  }
}
