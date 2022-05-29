(loop [x 0  ; x: variable to be looped, 0: initial value
       foo "bar"] ; any other variable as necessary
  (when (< x 10)
    (println x)
    (recur (inc x) "baz") ; recur goes to the next loop iteration
    ))