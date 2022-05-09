import 'package:flutter_bloc/flutter_bloc.dart';

/**
 * state: actual value of the Cubit
 * emit: notify subscribers about the state change
 */

class CounterCubit extends Cubit<int> {
  CounterCubit() : super(0); // initial state is 0

  void increment() {
    emit(state + 1);
  }

  void decrement() {
    emit(state - 1);
  }
}
