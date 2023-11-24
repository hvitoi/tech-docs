(require '[schema.core :as s])
(require '[schema-generators.generators :as g])
(require '[clojure.test.check.generators :as gen])


;; generate samples from schemas
(def Person
  "Schema for a Person"
  {:id s/Int,
   :name s/Str
   :uuid java.util.UUID
   :height java.math.BigDecimal})

(g/sample 3 Person) ; a sequence with 3 elements


;; custom generators
(def bigdecimal-generator (gen/fmap #(java.math.BigDecimal. %) gen/double))
(def uuid-generator (gen/return (java.util.UUID/randomUUID)))

(def leaf-generators {java.math.BigDecimal bigdecimal-generator
                      java.util.UUID uuid-generator})

(g/sample 3 Person leaf-generators)
