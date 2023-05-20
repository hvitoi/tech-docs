; executes repeatedly body (presumably for side-effects)

(doseq [x [1 2 3]
        y ["a" "b" "c"]]
  (println x y)) ; 9 loops

(doseq [i {:a {"a" "c"}
           :b "b"}]
  (println i)) ; iterate over the [key value]

(doseq [n (range 10)
        :let [i (-> n
                    inc
                    range
                    rand-nth)]]
  (println i))

(doseq [x {:a 1 :b 2}]
  (println x)); 9 loops
