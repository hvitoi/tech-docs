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

val transformInt: Int => Int =
  (x: Int) => {
    x * x * x
  }
