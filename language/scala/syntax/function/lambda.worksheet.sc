def transformInt(x: Int, f: Int => Int): Int = {
  f(x)
}

// Lambda functions / Anonymous functions / Function literals
transformInt(1, x => x * x * x)

transformInt(1, x => { val y = x * 2; y * y })
