;; lists make up the code in Clojure

;(1 2 3 4)
;(1 "two" 'three (1 2 3 4))
(defn foo [] (println "hello")) ; a list that is interpreted
(foo) ; if the first element (function position) in a list is the name of a function, then the function is executed
