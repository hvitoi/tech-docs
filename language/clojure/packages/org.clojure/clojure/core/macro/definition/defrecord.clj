;;
; Define a Record
(defrecord Person [id name age])

;;
; Constructor
(Person. 1 "Henry" 27) ; same
(->Person 1 "Henry" 27) ; same
(map->Person {:id 1, :name "Henry", :age 27}) ; same


;;
; Force parameter types
(defrecord Animal [^Long id,
                   ^String name,
                   ^Long age])

;;
;; Implement an interface
(defprotocol Printable
  (my-print-function) [arg1 arg2 arg3])
(defrecord Person [id name age]
  Printable
  (my-print-function
    [person a b]
    (println "Person:" (:name person))))


;;
; Access java fields
(def p (Person. 1 "Henry" 27))
(.name p)
