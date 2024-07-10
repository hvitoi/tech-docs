((some-fn even?) 1)
((some-fn even?) 2)

; tries the first argument (results false), then tries the second argument (returns true)
; it returns the first true result (if any)
((some-fn even?) 1 2)
((some-fn even?) 1 1)
