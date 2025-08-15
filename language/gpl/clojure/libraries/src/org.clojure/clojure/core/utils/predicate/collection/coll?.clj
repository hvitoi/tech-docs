(coll? "foo")                ; false
(coll? {})                   ; true
(coll? ["a" "b" "c"])        ; true
(coll? #{"a" "b" "c"})       ; true
(coll? (seq ["a" "a" "c"]))  ; true
(coll? (list ["a" "a" "c"])) ; true
