(require '[schema.core :as s])

(def Person
  "Schema for a Person"
  {:id (s/constrained s/Int pos? 'optional-name-for-the-predicate), ; must be s/Int. In this schema, it's constrained to those who obey the predicate
   :name s/Str})

; new schema
(def ValorFinanceiro (s/constrained s/Num pos?))