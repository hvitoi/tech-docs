;; add/modify elements in a nested element
;; only one item can be added at a time (differently from assoc)

;; map
(def my-map {:a 1 :b {:b1 8 :b2 9} :c 2})


(assoc-in my-map [:b :b3] 10) ; add new element
(assoc-in my-map [:b :b1] 7) ; modify existing element


;; vector
(def my-vector [0 1 [2 3]])

(assoc-in my-vector [2 0] 9) ; modify existing element

