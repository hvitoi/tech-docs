(require '[schema.core :as s])

(s/set-fn-validation! true)

;; Define a function
(s/defn simple-test :- Long ; return value is "Long"
  [x :- Long] ; "x" implements the schema "Long"
  x)

;; Define pre and post conditions
(s/defn simple-test :- Long
  [x :- Long]
  [y :- Long]
  ;; conditions (guarantees in runtime) - Otherwise throw AssertionError
  {:pre [(= x y), (= x 0)] ;; validate before the function is executed; inputs "x and y" must be equal and they must be 0
   :post [(= 0 %)]} ;; validate after the function is executed; % is the return value!

  x)

; the validation if performed when the function is called
(simple-test 9) ; ok
(simple-test "a") ; exception





(s/defschema Book {:book/id    s/Uuid
                   :book/title s/Str
                   :book/author s/Str
                   :book/genre  s/Str})

;; A function to initialize an object based on a schema
(s/defn new-book :- Book
  [title :- s/Str
   author :- s/Str
   genre :- s/Str]
  {:book/id (java.util.UUID/randomUUID)
   :book/title title
   :book/author author
   :book/genre genre})
(new-book "Adventure of Mr's Henry" "Henry" "Drama")