import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

class CounterContainer extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (_) => CounterCubit(),
      child: CounterView(),
    );
  }
}

class CounterView extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // subscribe to changes in the state and dynamically build/reload
    return BlocBuilder<CounterCubit, int>(
      builder: (ctx, state) {
        return Text(state.toString());
      },
    );
  }
}

class CounterView2 extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    // instead of getting the cubit from the context, you can specify it directly
    return BlocBuilder<CounterCubit, int>(
      bloc: CounterCubit(),
      builder: (ctx, state) {
        return Text(state.toString());
      },
    );
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
