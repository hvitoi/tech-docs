; similar to dorun, but returns nil instead
(dorun
 (map #(do (println "foo") %)
      (range 5)))
