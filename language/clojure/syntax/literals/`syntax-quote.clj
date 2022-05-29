; syntax-quote
; same as quote (') but also shows the namespace (for symbols)

`a ; => user/a
`"a" ; => "a" (same as '"a", because it's not a symbol, it's a value/string)
`(1 2 3) ; (1 2 3) (same as '(1 2 3) because it's not a symbol, it's a value/list)


;; unquote(~): define a symbol to be evaluated
`(a b (+ 1 2)) ; => (user/a user/b (clojure.core/+ 1 2))
`(a b ~(+ 1 2)) ; => (user/a user/b 3)

;; unquote-splicing (~@): break a list into its components (not evaluated)
(def data '((+ 1 1) (+ 2 2)))
`(a b ~@data)
