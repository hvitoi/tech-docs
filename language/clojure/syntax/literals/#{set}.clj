#{} ; empty set
#{1 32 1.5 "pet" 'cat}

;; define
(def my-set #{"a" "b" "c"})

;; access
(my-set "a") ; "a"
(my-set "d") ; nil


; Sets are functions!
(my-set "a") ; return the element (if found)
(my-set "d") ; nil

(some my-set ["a" "b" "z"]) ; "a" (the first element)
