;; Given a map "m" and a function "f" (with one arg), returns a new map where the keys 
;; of "m" are mapped to result of applying f to the corresponding values of m.
(update-vals {:a 1 :b 2} inc)
