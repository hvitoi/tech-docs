(list? "foo")                ; false
(list? {})                   ; false
(list? ["a" "b" "c"])        ; false
(list? #{"a" "b" "c"})       ; false
(list? (seq ["a" "a" "c"]))  ; false
(list? (list ["a" "a" "c"])) ; true
