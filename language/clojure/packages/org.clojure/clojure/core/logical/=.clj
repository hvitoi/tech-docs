(= 1 1)

(= {:a "a" :b "b"} {:a "a" :b "b"}) ; true

(= [1 2 3] '(1 2 3)) ; true

(= [1 2 3] #{1 2 3}) ; false

(= clojure.lang.PersistentQueue/EMPTY) ; true