(sequential? "foo")                ; false
(sequential? {})                   ; false
(sequential? ["a" "b" "c"])        ; true
(sequential? #{"a" "b" "c"})       ; false
(sequential? (seq ["a" "a" "c"]))  ; true
(sequential? (list ["a" "a" "c"])) ; true
