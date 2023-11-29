(require '[clojure.test :as test])

(defn spiral-matrix
  [n]
  (loop [matrix (vec (map (fn [_] (vec (repeat n false))) (range n)))
         num 1
         direction :right
         position [0 0]]
    (if (> num (* n n))
      matrix
      (let [next-num (inc num)
            next-direction (case direction
                             :right (if (false? (get-in matrix (update position 1 inc)))
                                      :right
                                      :down)
                             :down (if (false? (get-in matrix (update position 0 inc)))
                                     :down
                                     :left)
                             :left (if (false? (get-in matrix (update position 1 dec)))
                                     :left
                                     :up)
                             :up (if (false? (get-in matrix (update position 0 dec)))
                                   :up
                                   :right))
            next-position (case next-direction
                            :right (update position 1 inc)
                            :down (update position 0 inc)
                            :left (update position 1 dec)
                            :up (update position 0 dec))]
        (recur
         (assoc-in matrix position num)
         next-num
         next-direction
         next-position)))))

(test/deftest spiral-matrix-test
  (test/testing "Return a spiral matrix"
    (test/is (= [[1   2  3  4]
                 [12 13 14  5]
                 [11 16 15  6]
                 [10  9  8  7]]
                (spiral-matrix 4)))))

(test/run-test spiral-matrix-test)
