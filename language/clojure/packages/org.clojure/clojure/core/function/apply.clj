
; apply a function with its args
; can be used to force a lazy seq
(apply + [1 2 3]) ; the list contains the params for the "+" function. arg1=1, arg2=2, arg3=3
(+ 1 2 3) ; same

(apply str [1 1 2 3 5 8 13 21])
