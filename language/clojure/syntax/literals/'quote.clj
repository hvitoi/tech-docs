;; receive and return anything (without evaluating)

'nil
'(0 1 2 3 4 5) ; list
'"a" ; string
'(str "hey" "there" (+ 1 1)) ; sexp
'a ; simple symbol
'a/b ; namespaced symbol
'a???.#! ; most punctuation is allowed

(quote a) ; same
