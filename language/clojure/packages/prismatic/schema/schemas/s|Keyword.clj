(require '[schema.core :as s])

(s/validate s/Keyword :a) ; ok
(s/validate s/Keyword 15) ; fail
