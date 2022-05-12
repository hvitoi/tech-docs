;; Equivalent to an Interdace in Java

;; Printable Interface
(defprotocol Printable
  (my-print-function) [this arg2 arg3]) ; first arg is the object instance itself

;; Person implements Printable
(defrecord Person [id name age])
(extend-type Person
  Printable ; interface to implement
  (my-print-function ; implementation of functions of that interface
    [person a b]
    (println "Person:" (:name person))))

;; Animal implements Printable
(defrecord Animal [id name age])
(extend-type Animal
  Printable ; interface to implement
  (my-print-function ; implementation of functions of that interface
    [animal a b]
    (println "Animal:" (:name animal))))

;; Instances
(let [p (->Person 1 "Henry" 27)]
  (my-print-function p "a" "b")) ; call the implementation of the Person class

(let [a (->Animal 2 "Doggy" 3)]
  (my-print-function a "a" "b")) ; call the implementation of the Animal class
