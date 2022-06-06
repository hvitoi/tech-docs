// Functions
def squareIt(x: Int): Int = {
  x * x // last evaluation is the return value
}

def cubeIt(x: Int): Int = { x * x * x }

println(squareIt(2))
println(cubeIt(3))

// Function that receives a function
def transformInt(x: Int, f: Int => Int): Int = {
  f(x)
}

val result = transformInt(2, cubeIt)
println(result)

// Lambda functions / Anonymous functions / Function literals
transformInt(3, x => x * x * x)

transformInt(10, x => x / 2)

transformInt(2, x => { val y = x * 2; y * y })
