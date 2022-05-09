; currying! Reduce the number of args of a function
; similar to "bind" in javascript

(defn give-me-3
  [item1 item2 item3]
  {:a item1
   :b item2
   :c item3})

(def give-me-2 (partial give-me-3 "1st item"))
(def give-me-1a (partial give-me-2 "2nd item")) ; same
(def give-me-1b (partial give-me-3 "1st item" "2nd item")) ;same

(give-me-1a "3rd item")
(give-me-1b "3rd item")