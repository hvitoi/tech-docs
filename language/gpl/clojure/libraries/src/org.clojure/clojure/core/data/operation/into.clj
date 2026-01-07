;; take all nested values from the second form and insert into the map on the first form

(into {} [[:a 1] [:c 3] [:b 2]])
(into {} [{:a 1} {:c 3} {:b 2}])
(into {} [{:a 1} {:c 3} {:b 2}])
(into {:a 1} {:b 2 :c 3})

(into [] {:a 1 :b 2}) ; don't!
(vec {:a 1 :b 2}) ; use this instead


;; using a transducer

; adds 2, then filter only odd numbers
(def xform (comp (map #(+ % 10))
                 (filter odd?)))
(into [-1 -2] xform (range 10))

(into [] cat [[1 2] [3 4]]) ;; "cat" built-in transducer
