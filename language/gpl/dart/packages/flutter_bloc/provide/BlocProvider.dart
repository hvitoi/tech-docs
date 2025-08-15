import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

/**
 * The Container joins together the "cubit" (CounterCubit) and the "widget" (CounterView)
 * BlocProvider add to the "context" info to access the cubit
 */
class CounterContainer extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (BuildContext ctx) {
        final cubit = CounterCubit();
        return cubit;
      },
      child: CounterView(),
    );
  }
}

/**
 * BlocProvider.value
 */

// Receives a cubit that was already created from the context

class CounterContainer2 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BlocProvider.value(
      value: BlocProvider.of<CounterCubit>(context), // receive cubit from ctx
      // value: CounterCubit(), // No!! To create cubit directly use the conventional BlocProvider
      child: CounterView(),
    );
  }
}

// ---

class CounterView extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // call method from the cubit
    context.read<CounterCubit>().increment();

    // access state
    int val = context.read<CounterCubit>().state;

    return Text(val.toString());
  }
}

class CounterCubit extends Cubit<int> {
  CounterCubit() : super(0);

  void increment() {
    emit(state + 1);
  }

  void decrement() {
    emit(state - 1);
  }
}
