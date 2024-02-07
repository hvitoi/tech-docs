(def data [{:name "john", :age 16 :children ["a" "b"]}
           {:name "mark", :age 16 :children ["a"]}
           {:name "jeff", :age 18 :children []}])

;; group-by keyword
(group-by :age data)
; {16 [{:name "john", :age 16} {:name "mark", :age 16}], 18 [{:name "jeff", :age 18}]}


;; group-by aggregation function
(defn my-agg-fn [el] (count (:children el)))

(group-by my-agg-fn data)
