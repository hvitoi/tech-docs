(vector? "foo")                ; false
(vector? {})                   ; false
(vector? ["a" "b" "c"])        ; true
(vector? #{"a" "b" "c"})       ; false
(vector? (seq ["a" "a" "c"]))  ; false
(vector? (list ["a" "a" "c"])) ; false
