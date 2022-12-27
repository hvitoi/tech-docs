def transformInt(x: Int, f: Int => Int): Int = {
  f(x)
}

// Lambda functions / Anonymous functions / Function literals
transformInt(3, x => x * x * x)

transformInt(10, x => x / 2)

transformInt(2, x => { val y = x * 2; y * y })
