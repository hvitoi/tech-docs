; composite of functions, return another function

; first evaluate "=" and then "not"
(def not-equal? (comp not =))
