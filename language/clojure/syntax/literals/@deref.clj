;; dereference
;; deref `is used for dereferencing a lot of different reference types, including futures, atoms, etc

(def my-atom (atom "abc"))
(println @my-atom)
(println (deref my-atom)) ; same output