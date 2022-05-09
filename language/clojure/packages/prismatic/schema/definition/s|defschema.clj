(require '[schema.core :as s])

;; like "def", but makes clear that a schema is being created

(s/defschema Person
  "Schema for a Person"
  {:id s/Int,
   :friends [s/Str]
   :name s/Str})


; BACKWARD + FORWARD COMPATIBLE by default
;; Schema for maps
(def Person
  "Schema for a Person"
  {:id s/Int, ; keywords are mandatory by default
   :uuid java.util.UUID ; accepts java types
   :height java.land.BigDecimal
   :friends [s/Str]
   :name s/Str})

(s/validate Person {:id 1, :name "Henry"}) ; ok
(s/validate Person {:id 1, :name "Henry", :age 27}) ; fail

;; Schema for dynamic maps
(def Person
  {s/Num s/Str})

(s/validate Person {1 "a", 2 "b"}) ; ok
(s/validate Person {1 "a", "b" "b"}) ; fail

;; Schema for vectors
(def NumVector
  [s/Num])

(s/validate NumVector [1 2 3]) ; ok
(s/validate NumVector []) ; ok
(s/validate NumVector nil) ; ok (nil is an empty sequence)

