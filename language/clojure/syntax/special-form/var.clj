(def a "a")

; access the symbol (not its value)
(var a)
(var "a") ; fail! it's not a symbol (it's a value)
#'a ; same
