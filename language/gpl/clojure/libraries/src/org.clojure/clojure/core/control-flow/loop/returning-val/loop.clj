(loop [x 0  ; bindings with the initial values
       y :foo]
  (if (> x 10)
    [x y]
    (recur (inc x) :bar))) ; recur goes to the next loop iteration
