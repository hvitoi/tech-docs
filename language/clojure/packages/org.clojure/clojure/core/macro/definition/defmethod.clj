; function with many implementations
; to strategy must be defined in order to choose which implementation to pick 
(defmulti my-fn class) ; use "class" function as strategy

; implementations
(defmethod my-fn
  java.lang.String ; argument that will be passed to the strategy
  [item]
  (println "String:" item))

(defmethod my-fn
  java.lang.Number ; argument that will be passed to the strategy
  [item]
  (println "Number:" item))

;; invoking methods
(my-fn 99)
(my-fn "abc")