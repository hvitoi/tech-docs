(def my-atom (atom "abc")) ; clojure.lang.Atom

; access value of an atom with @
(println @my-atom)
(instance? clojure.lang.IDeref my-atom)

(def counter (atom 0))
(swap! counter inc)
