;; add/modify elements (with a value)
;; allows accessing nested values
;; only one item can be added at a time (differently from assoc)

;; map
(assoc-in {:a 1 :b {:b1 21 :b2 22} :c 3} [:b :b3] 23) ; add new element
(assoc-in {:a 1 :b {:b1 21 :b2 22} :c 3} [:b :b1] 7) ; modify existing element
(assoc-in {:a 1 :b {:b1 21 :b2 22} :c 3} [:b] {:b3 23}) ; replace everything in b

;; vector
(assoc-in [0 1 [20 21]] [2 0] 100) ; modify existing element
