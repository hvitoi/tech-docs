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






;; comment macro
(defmacro comment
  "Ignores body, yields nil"
  {:added "1.0"}
  [& body])

;; when macro
(defmacro when
  "Evaluates test. If logical true, evaluates body in an implicit do"
  {:added "1.0"}
  [test & body]
  (list 'if test (cons 'do body)))
