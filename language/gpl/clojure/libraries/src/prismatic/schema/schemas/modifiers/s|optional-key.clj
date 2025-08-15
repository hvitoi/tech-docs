(require '[schema.core :as s])

(def Person
  "Schema for a Person"
  {:id s/Num,
   (s/optional-key :name) s/Str}) ; optional key

(s/validate Person {:id 1, :name "Henry"}) ; ok
(s/validate Person {:id 1}) ; ok