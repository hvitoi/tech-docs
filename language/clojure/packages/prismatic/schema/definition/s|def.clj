(require '[schema.core :as s])

;; define a symbol and validate its value
(s/def foo :- long
  "a long"
  2)

