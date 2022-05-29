; clojure.lang.IFn

(defn my-function
  "This is a function" ; description of the function (optional)
  {:doc "Docs can be added like this too" ; attribute map
   :foo "Any attributes you fancy"
   :test (fn [] ; test runners will pick this
           (clojure.test/is (= "anything" (my-function "bla")))
           (clojure.test/is (= "anything" (my-function "ble"))))}
  [& args] ; arguments (list of zero or more args)
  (println "My args:" args) ; expression
  (+ 2 3) ; expression 
  "anything" ; return value (the last expression)
  )
(my-function "a" "b" "c") ; execute
(meta #'my-function) ; metadata
(clojure.repl/doc my-function) ; documentation
(clojure.test/test-var #'my-function) ; run tests from attribute map

;; Private Functions: accessible inside the namespace (start with -)
(defn -main
  []
  (println "hello"))
(-main)

;; Predicate functions: functions that return true/false (end with ?)
(defn apply-discount?
  [full-price]
  (> full-price 100))

;; Multi-arity functions: overload constructor
(defn hello
  ([] (hello "World"))
  ([s] (str "Hello " s "!")))
(hello)
(hello "Clojure Friend")

(defn sum-coordinates
  ([c]
   (sum-coordinates {:x 0 :y 0} c)) ; ”identity” value for a function
  ([c1 c2]
   {:x (+ (:x c1) (:x c2))
    :y (+ (:y c1) (:y c2))}))

;; Variadic functions: arbitrary number of arguments
(defn lead+members
  [lead & members]
  {:lead lead
   :members members}) ; members is received as a list
(lead+members "Dave Mustain" ; lead
              "Marty Friedman" ; member
              "Nick Menza" ; member
              "David Ellefson") ; member
