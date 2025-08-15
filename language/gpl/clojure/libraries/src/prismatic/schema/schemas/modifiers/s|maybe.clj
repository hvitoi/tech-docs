(require '[schema.core :as s])

; may return nil
; use only for function return value!
; for input parameters use s/optional-key instead

(s/validate (s/maybe s/Keyword) :a) ; ok
(s/validate (s/maybe s/Keyword) nil) ; ok
(s/validate (s/maybe s/Keyword) "a") ; fail
