;; an example of looking up a value from a
;; map and performing an operation(addition)
;; on it if it exists
(some->> {:y 3 :x 5}
         (:y)
         (- 2))



;; if we were to look up a value which
;; doesn't exist, it will safely short-circuit
(some->> {:y 3 :x 5}
         (:z)
         (- 2))

