(require '[schema.core :as s])

(s/validate s/Num 15) ; ok
(s/validate s/Num "abc") ; fail
