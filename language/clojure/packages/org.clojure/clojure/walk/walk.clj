(require '[clojure.walk :as walk])

(walk/walk #(* 2 %) #(apply + %) [1 2 3 4 5])
