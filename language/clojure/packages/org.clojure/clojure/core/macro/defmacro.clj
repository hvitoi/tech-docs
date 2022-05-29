;; macros receive the raw symbols
;; functions receive the calculated values from the symbols

(defmacro my-macro
  "macro documentation"
  [arg1 arg2 arg3] ;; raw symbols (or values)
  (println arg1 arg2 arg3) ;; print symbols
  [arg1 arg2 arg3]) ;; symbols are evaluated only on the final return

(def name "Henry")
(def number 10)
(my-macro name "blabla" (+ 1 number))
; => print the symbols: 'name "blabla" '(+ 1 number)
; => calculate the symbols ["Henry" "blabla" 11]


;; -----

(defmacro my-macro
  [arg1 arg2 arg3]
  (list arg1 arg2 arg3))
(my-macro str "hey" "there")
; => evaluate the list generated (str "hey" "there")

;; -----

;; comment macro
(defmacro comment
  "Ignores body, yields nil"
  {:added "1.0"}
  [& body])

;; -----

;; when macro (if true (do "hello" "hey"))
(defmacro when
  [test & body]
  (list 'if test (cons 'do body))) ; 

(defmacro when ; same effect
  [test & body]
  `(if ~test ~(cons 'do body)))

(defmacro when ; same effect
  [test & body]
  `(if ~test (do ~@body)))

(defmacro when ; same effect
  [test & body]
  (let [my-symbol (gensym)] ; good for avoiding shadowing other symbols inside of a macro
    `(if ~test
       (let [~my-symbol "Henry"]
         (println ~my-symbol) ; step not defined by the user
         (do ~@body)))))

(defmacro when ; same effect
  [test & body]
  `(if ~test
     (let [random-symbol# "Henry"] ; auto-gensym: generates a random symbol on the fly (can only be used inside of a macro)
       (println random-symbol#)
       (do ~@body))))
