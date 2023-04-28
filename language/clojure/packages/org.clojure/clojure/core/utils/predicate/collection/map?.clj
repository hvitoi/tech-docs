(map? "foo")                ; false
(map? {})                   ; true
(map? ["a" "b" "c"])        ; false
(map? #{"a" "b" "c"})       ; false
(map? (seq ["a" "a" "c"]))  ; false
(map? (list ["a" "a" "c"])) ; false
