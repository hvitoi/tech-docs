;; add/modify elements

;; map
(def data {:k1 "v1", :k2 "v2"})
(assoc data :k3 "v3") ; add new element
(assoc data :k3 "v3" :k4 "v4") ; add multiple elements
(assoc data :k2 "blabla") ; modify existing element


;; vector
(def data2 ["a" "b" "c"])
(assoc data2 3 "z") ; add new element (only to the last position + 1)
(assoc data2 3 "y" 4 "z") ; add multiple elements
(assoc data2 0 "z") ; modify existing element (index 0)
(assoc data2 3 (+ 1 1)) ;; assoc with a function evaluation
