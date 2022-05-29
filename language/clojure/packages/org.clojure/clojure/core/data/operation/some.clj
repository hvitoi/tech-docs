; Returns true if at least the predicate for at least 1 element returns true
; Returns nil otherwise

;; vector
(some #(> % 0) [-1 0 1]) ; if at least one element is greater than zero

;; map
(some #(> (second %) 0) {:a -1, :b 0, :c 1}) ; if at least one element is greater than zero

;; set as a predicate
(def my-set #{"a"})
(some my-set ["a" "b" "z"])
