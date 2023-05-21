(seqable? "foo")                ; true
(seqable? {})                   ; true
(seqable? ["a" "b" "c"])        ; true
(seqable? #{"a" "b" "c"})       ; true
(seqable? (seq ["a" "a" "c"]))  ; true
(seqable? (list ["a" "a" "c"])) ; true
