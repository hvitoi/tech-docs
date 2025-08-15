(require '[schema-generators.generators :as g])


(def Person
  "Schema for a Person"
  {:id s/Int,
   :name s/Str})

; only one element
(g/generate Person)
