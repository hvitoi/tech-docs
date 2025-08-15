(require '[schema.core :as s])

;; Declarative way to impose a restriction for a schema

;; Create a schema with a predicate
(def PositiveNumber (s/pred #(> % 0))) ; if the predicate is defined as a lambda, on error message it will have unknown name

(s/validate PositiveNumber 1) ; ok
(s/validate PositiveNumber -1) ; fail
