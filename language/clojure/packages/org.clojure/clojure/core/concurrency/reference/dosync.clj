(def a (ref 100))


; creates a transaction
(dosync
 (ref-set a 110))

(dosync
 (alter a inc))

(println @a)