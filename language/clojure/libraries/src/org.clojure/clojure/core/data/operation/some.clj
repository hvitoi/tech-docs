; Returns the first truthy value, otherwise nil

;; vector
(some #(> % 2) [0 1 2 3 4])
(some identity [false nil 4 5])

;; map
(some #(> (second %) 0) {:a -1, :b 0, :c 1}) ; if at least one element is greater than zero

;; set as a predicate
(def my-set #{"a"})
(some my-set ["a" "b" "z"])

(some #(contains? #{:a} %) [:a :b :c])
