;; take all nested values from the second form and insert into the map on the first form

(into {} [[:a 1] [:c 3] [:b 2]])
(into {} [{:a 1} {:c 3} {:b 2}])
(into {} [{:a 1} {:c 3} {:b 2}])
(into {:a 1} {:b 2 :c 3})

(into [] {:a 1 :b 2}) ; don't!
(vec {:a 1 :b 2}) ; use this instead
