;; dereference: used for dereferencing a lot of different reference types, including futures, atoms, etc

;; atom
(def data (atom "abc"))
@data
(deref data) ; same output
