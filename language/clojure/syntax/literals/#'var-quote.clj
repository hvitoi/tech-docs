;; receive and return a reference to the symbol clojure.lang.Symbol (without evaluating it)

#'a ; access the symbol (not its value)
#'"a" ; fail! not a symbol
