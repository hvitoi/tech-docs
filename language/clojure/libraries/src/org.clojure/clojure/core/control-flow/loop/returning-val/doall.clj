; returns the result of evaluating an expression
(doall
 (map #(do (println "foo") %)
      (range 5)))
