
(def ^:dynamic *foo*
  {})

(binding
 [*foo* "bar"]
  *foo*)
