;; add/modify elements

;; map
(def my-map {:k1 "v1", :k2 "v2"})

(assoc my-map :k3 "v3") ; add new element
(assoc my-map :k3 "v3" :k4 "v4") ; add multiple elements
(assoc my-map :k2 "blabla") ; modify existing element


;; vector
(def my-vector ["a" "b" "c"])

(assoc my-vector 3 "z") ; add new element (only to the last position + 1)
(assoc my-vector 3 "y" 4 "z") ; add multiple elements
(assoc my-vector 0 "z") ; modify existing element (index 0)


;; assoc with a function evaluation
(assoc my-vector 3 (+ 1 1))