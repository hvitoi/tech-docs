(def a (ref 100))


; creates a transaction
(dosync
 (ref-set a 110))

(dosync
 (alter a inc))

(println @a)


;; -----

(def my-ref (ref 9))

; to change a ref, the operations must be inside a transaction
; create a transaction with dosync
(dosync
 (ref-set my-ref 10))

(println @my-ref)