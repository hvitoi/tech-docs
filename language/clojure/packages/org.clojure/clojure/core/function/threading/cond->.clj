(cond-> 1        ; we start with 1
  true inc       ; the condition is true so (inc 1) => 2
  false (* 42)   ; the condition is false so the operation is skipped
  (= 2 2) (* 3))
