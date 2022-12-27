val foo: String = "a,b,c"
val bar: Array[String] = foo.split(",")
val baz: Array[String] = foo.split("\\W+") // split entire words (regex)
