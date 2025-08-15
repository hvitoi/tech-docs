(doseq [x [1 2 3]
        y ["a" "b" "c"]]
  (println x y)
  [x y]) ; 9 loops

(doseq [i {:a {"a" "c"}
           :b "b"}]
  (println i)) ; iterate over the [key value]

(doseq [[foo bar] {:foo 1 :bar 2}]
  (println foo bar))

(doseq [n (range 10)
        :let [i (-> n
                    inc
                    range
                    rand-nth)]]
  (println i))

(doseq [x {:a 1 :b 2}]
  (println x)); 9 loops
