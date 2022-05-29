;; Often used to "short-circuit out" of a series of steps:
;; When nil is returned by any step, the further steps are not executed
;; Thus the nil case need be handled only once, at the end.
(some-> val
        step1
        step2
        step3)
