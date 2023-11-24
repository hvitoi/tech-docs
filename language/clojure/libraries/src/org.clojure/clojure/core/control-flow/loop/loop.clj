 (loop [x 0  ; bindings with the initial values
        y "foo"]
   (when (< x 10)
     (println x y)
     (recur (inc x) "bar"))) ; recur goes to the next loop iteration

(loop []
  (println "printing forever very fast")
  (recur))
