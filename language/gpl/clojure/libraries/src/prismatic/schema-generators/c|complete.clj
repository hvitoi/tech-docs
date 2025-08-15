(require '[schema-generators.complete :as c])

(def Person
  "Schema for a Person"
  {:id s/Int,
   :name s/Str})

; force a property
(c/complete {:name "Henry"} Person)
