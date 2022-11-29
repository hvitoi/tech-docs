(require '[clojure.walk :as walk])

; 1st function: pass throw all the items
; 2st function: reduce the result

(walk/walk #(* 2 %) #(apply + %) [1 2 3])
(walk/walk (fn [[k v]] [k (* 2 v)]) identity {:a 1 :b 2 :c 3})
