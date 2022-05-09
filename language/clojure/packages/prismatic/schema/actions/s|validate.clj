(ns app.validate
  (:require [schema.core :as s]))

; if valid, return the symbol itself
(s/validate Long 15)

; if invalid, throws exception
(s/validate Long "abc")

; if valid, return the symbol itself
(s/validate java.lang.Long 15)
(s/validate Long 15)

; if invalid, throws exception
(s/validate java.lang.Long "abc")
(s/validate Long "abc")