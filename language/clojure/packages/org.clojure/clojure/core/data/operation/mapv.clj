;; Forces a map to be completely eager
;; This way the map is executed right away
;; The normal map execute in chunks of 32 elements
; it's used for operations with side effects

;; sequence
(mapv println (range 50))
