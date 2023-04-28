(indexed? "foo")                ; false
(indexed? {})                   ; false
(indexed? ["a" "b" "c"])        ; true
(indexed? #{"a" "b" "c"})       ; false
(indexed? (seq ["a" "a" "c"]))  ; false
(indexed? (list ["a" "a" "c"])) ; false
