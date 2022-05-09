(require '[schema.core :as s])

(s/validate s/Int 15) ; ok
(s/validate s/Int "abc") ; fail
