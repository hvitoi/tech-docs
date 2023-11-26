(require '[clojure.math :as math])

;; returns the least integer greater than or equal to n.
;; If n is an exact number, ceil returns an integer, otherwise a double.

(math/ceil 1.2)
