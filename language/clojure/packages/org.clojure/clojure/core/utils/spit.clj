
; write to file to project root
(spit "foo.txt" "lala")
(spit "foo.txt" "lele" :append true)

(slurp "foo.txt")