
;; vector
(def my-vector ["a" "b" "c"])

; verify if an index exists
(contains? my-vector 2) ; true
(contains? my-vector 3) ; false

;; map
(def my-map {:a "a", :b "b"})

; verify if a keyword exists
(contains? my-map :a) ; true
(contains? my-map :z) ; false