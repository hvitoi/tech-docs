(require '[clojure.walk :refer :all])

; traverse a collection (depth first)

;; vector
(def matrix [[1 [2 3]]
             [4 5 6]
             [7 8 9]
             10])
(prewalk #(if (number? %) (inc %) %) matrix)


;; map
(def my-nested-map {:alpha {:beta 1} :gamma 2})
(prewalk #(if (number? %) (inc %) %) my-nested-map)
