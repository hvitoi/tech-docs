(associative? "foo")                ; false
(associative? {})                   ; true
(associative? ["a" "b" "c"])        ; true
(associative? #{"a" "b" "c"})       ; false
(associative? (seq ["a" "a" "c"]))  ; false
(associative? (list ["a" "a" "c"])) ; false
