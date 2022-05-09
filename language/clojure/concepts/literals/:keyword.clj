:alpha ; simple keyword 
:release/alpha ; namespaced keyword 

;; access value in a keyword
(def my-map {:alpha "a" :beta "b"})
(:alpha my-map)
(:alpha my-map 15) ; default value
