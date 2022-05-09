(ns require '[schema.core :as s])

(s/validate s/Str "abc") ; ok
(s/validate s/Str 15) ; fail
