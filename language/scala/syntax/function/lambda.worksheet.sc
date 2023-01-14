def transformInt(x: Int, f: Int => Int): Int = {
  f(x)
}

// Lambda functions / Anonymous functions / Function literals
val myLambda = (x: Int) => { x * x * x }
val myLambda2 = (x: Int) => { val y = x * 2; y * y }

transformInt(1, myLambda)
transformInt(1, myLambda2)
