(require '[clojure.test :as test]
         '[clojure.math :as math])

(defn planted-all-seeds?
  [flowerbed seeds]
  (let [leftover-seeds (atom seeds)]
    (reduce
     (fn [prev-plot plot]
       (let [can-plant? (and (zero? plot)
                             (zero? prev-plot))]
         (if can-plant?
           (do (swap! leftover-seeds dec)
               1)
           plot)))
     0 flowerbed)
    (<= @leftover-seeds 0)))

(defn planted-all-seeds?*
  [flowerbed seeds]
  (let [total-plots (count flowerbed)
        plantable-plots (math/ceil (/ total-plots 2))
        filled-plots (reduce (fn [count plot]
                               (if (= 1 plot)
                                 (inc count)
                                 count))
                             0 flowerbed)
        available-plots (- plantable-plots filled-plots)]
    (>= available-plots seeds)))

(test/deftest planted-all-seeds?-test
  (test/testing ""
    (test/is (true?
              (planted-all-seeds? [1,0,0,0,1] 1)))
    (test/is (false?
              (planted-all-seeds? [1,0,0,0,1] 2))))
  (test/testing "Alternative solution"
    (test/is (true?
              (planted-all-seeds?* [1,0,0,0,1] 1)))
    (test/is (false?
              (planted-all-seeds?* [1,0,0,0,1] 2)))))

(test/run-test planted-all-seeds?-test)
