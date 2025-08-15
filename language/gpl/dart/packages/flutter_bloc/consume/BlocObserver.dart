import 'package:flutter_bloc/flutter_bloc.dart';

/**
 * Subscribe to all stores
 * Similar to BlocBuilder, but outside of a widget
 */

class LogObserver extends BlocObserver {
  @override
  void onChange(BlocBase bloc, Change change) {
    print("Type: ${bloc.runtimeType}. New state: ${change}");
    super.onChange(bloc, change);
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
