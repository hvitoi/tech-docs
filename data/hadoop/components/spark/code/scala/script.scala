val nums = sc.parallelize(List(1,2,3,4))
val squared = nums.map(x => x*x).collect()
