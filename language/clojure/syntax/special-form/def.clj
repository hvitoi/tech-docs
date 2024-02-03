;; give a value to a symbols
;; symbols are shared between threads
;; root binding

; define a simple variable
(def my-symbol 9)

; can be redefined!
(def my-symbol "aa")

; define a function variable
(def increment (fn [x] (+ x 1)))

(increment 1)
