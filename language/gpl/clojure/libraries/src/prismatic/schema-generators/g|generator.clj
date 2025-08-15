(require '[schema-generators.generators :as g])


(def Person
  "Schema for a Person"
  {:id s/Int,
   :name s/Str})

; Creates a Generator from a Schema
(g/generator Person)
