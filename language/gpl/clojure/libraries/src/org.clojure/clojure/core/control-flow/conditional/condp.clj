(def my-num 3)

(condp = my-num
  1 "one"
  2 "two"
  3 "three"
  "something else")
