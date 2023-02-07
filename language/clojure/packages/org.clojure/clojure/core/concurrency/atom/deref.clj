(def my-atom (atom "abc"))

(println (deref my-atom))
(println @my-atom) ; same

(deref nil) ; exception!
