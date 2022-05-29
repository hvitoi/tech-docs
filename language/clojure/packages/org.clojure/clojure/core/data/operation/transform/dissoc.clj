;; remove element

;; map
(def my-map {:k1 "v1", :k2 "v2"})

(dissoc my-map :k1) ; remove element
(dissoc my-map :k1 :k2) ; remove elements
(dissoc my-map :k9) ; remove non-existent element


;; vector
(def my-vector ["a" "b" "c"])

(dissoc my-vector 0) ; remove element
