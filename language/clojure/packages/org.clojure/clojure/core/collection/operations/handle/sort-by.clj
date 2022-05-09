(def my-vector [{:name "john", :age 30 :children ["a" "b"]}
                {:name "mark", :age 28 :children ["a"]}
                {:name "jeff", :age 20 :children []}])

;; sort-by keyword
(sort-by :age my-vector)

;; sort-by with a function
(sort-by count ["aaa" "aa" "a"])
