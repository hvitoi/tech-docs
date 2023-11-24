(def my-ref (ref 9))

; update reference with a constant 
; to change a ref, the operations must be inside a transaction
; create a transaction with dosync
(dosync
 (ref-set my-ref 10))

(println @my-ref)