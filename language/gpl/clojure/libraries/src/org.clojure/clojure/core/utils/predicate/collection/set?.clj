(set? "foo")                ; false
(set? {})                   ; false
(set? ["a" "b" "c"])        ; false
(set? #{"a" "b" "c"})       ; true
(set? (seq ["a" "a" "c"]))  ; false
(set? (list ["a" "a" "c"])) ; false
