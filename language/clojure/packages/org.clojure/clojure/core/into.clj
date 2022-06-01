(into (sorted-map) [[:a 1] [:c 3] [:b 2]])

(defmacro a [& body] `(~body))

(a "a")