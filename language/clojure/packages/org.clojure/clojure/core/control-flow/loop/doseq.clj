; executes repeatedly body (presumably for side-effects)

(doseq [x [1 2 3]
        y ["a" "b" "c"]]
  (println x y)) ; 9 loops

(doseq [i {:a {"a" "c"} :b "b"}]
  (println i))
