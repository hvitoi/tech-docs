; same as ' but also shows the namespace (for symbols)

`a ; => user/a
`"a" ; => "a" (same as '"a", because it's not a symbol, it's a value/string)
`(1 2 3) ; (1 2 3) (same as '(1 2 3) because it's not a symbol, it's a value/list)


;; with ` it's possible to define a symbol to be evaluated with ~
`(a b (+ 1 2)) ; => (user/a user/b (clojure.core/+ 1 2))
`(a b ~(+ 1 2)) ; => (user/a user/b 3)