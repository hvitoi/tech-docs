;; add/modify elements in a nested element
;; only one item can be added at a time (differently from assoc)

;; map
(def data {:a 1 :b {:b1 8 :b2 9} :c 2})
(assoc-in data [:b :b3] 10) ; add new element
(assoc-in data [:b :b1] 7) ; modify existing element


;; vector
(def data2 [0 1 [2 3]])
(assoc-in data2 [2 0] 9) ; modify existing element

