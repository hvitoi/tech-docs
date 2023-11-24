(def my-ref (ref 8))

; update reference with a function 
(dosync
 (alter my-ref inc))

(println @my-ref)