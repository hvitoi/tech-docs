; currying! Reduce the number of args of a function
; similar to "bind" in javascript

(defn give-me-3
  [item1 item2 item3]
  `(~item1 ~item2 ~item3))

(def give-me-2 (partial give-me-3 "1st item"))
(def give-me-1a (partial give-me-2 "2nd item")) ; same
(def give-me-1b (partial give-me-3 "1st item" "2nd item")) ;same
(def give-me-0 (partial give-me-1a "3rd item"))

(give-me-0)

;;
(def plus-one
  (partial + 1))
(plus-one 10)

;;
(def with-abc-prefix
  (partial str "abc"))
(with-abc-prefix "henry")
