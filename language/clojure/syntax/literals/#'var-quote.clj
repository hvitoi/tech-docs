;; receive and return a reference to the symbol clojure.lang.Symbol (without evaluating it)
(def a "a")
#'a ; access the symbol (not its value)
(var a) ; same

#'"a" ; fail! not a symbol

#'(fn [])