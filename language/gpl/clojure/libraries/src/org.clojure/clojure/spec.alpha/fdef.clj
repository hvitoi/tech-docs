(require '[clojure.spec.alpha :as s])

;; fdef is a macro that defines a function specification
;; It describes the contract for a function: its arguments, return value, and optionally their relationship

(s/fdef my-function
  :args (s/cat :x int?)
  :ret int?)

(defn my-function
  [x]
  x)

(my-function "a")
(my-function 1)
