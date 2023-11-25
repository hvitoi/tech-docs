; Returns a vector of booleans representing the predicate for each element
; Similar to map, but with "keep", truthy values are converted to "true"

;; vector
(keep even? [0 1 2])
(map even? [0 1 2])
