(defmulti my-fn class)

(defmethod my-fn
  java.lang.String
  [item]
  (println "String:" item))

(defmethod my-fn
  java.lang.Number
  [item]
  (println "Number:" item))

(my-fn 99)
(my-fn "abc")


;; CUSTOM strategy
(defn custom-strategy
  [item]
  (if (= "a" item)
    :first-implementation
    :second-implementation))

(defmulti my-fn custom-strategy)
(defmethod my-fn
  :first-implementation
  [item]
  (println "First implementation:" item))
(defmethod my-fn
  :second-implementation
  [item]
  (println "Second implementation:" item))
(my-fn "a")
(my-fn "b")
