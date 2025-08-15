;; defmulti is a method with various implementation
;; defmethod defines each implementation
;; the implementation will be chosen based on the strategy

(defmulti greeting
  (fn [params] (:language params)) ; this is the strategy
  )

(defmethod greeting "english"
  [params]
  (str "Hello, " (:name params) "!"))

(defmethod greeting "french"
  [params]
  (str "Bonjour, " (:name params) "!"))

(greeting {:name "Henry" :language "english"}) ; hello
(greeting {:name "Fredericco" :language "french"}) ; bonjour

;; ----

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

(my-fn 99)
(my-fn "abc")