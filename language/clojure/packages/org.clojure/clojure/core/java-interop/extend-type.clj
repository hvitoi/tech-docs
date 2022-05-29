;; Printable Interface
(defprotocol Printable
  (my-print-function) [arg1 arg2 arg3])

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

;; Number implements Printable
(extend-type java.lang.Number
  Printable
  (my-print-function [this] (println this)))


;; Instances
(let [p (->Person 1 "Henry" 27)]
  (my-print-function p "a" "b")) ; call the implementation of the Person class

(let [a (->Animal 2 "Doggy" 3)]
  (my-print-function a "a" "b")) ; call the implementation of the Animal class

(let [n 99]
  (my-print-function n)) ; call the implementation of the Animal class