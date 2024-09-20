(require '[clojure.test :as test])

(defn avg
  [coll]
  (double (/ (reduce + coll) (count coll))))

(defn max-avg-subarray-i
  [nums k]
  (->> (inc (- (count nums) k))
       range
       (map #(subvec nums % (+ % k)))
       (map avg)
       sort
       last))

(test/deftest max-avg-subarray-i-test
  (test/testing ""
    (test/is (= 12.75000
                (max-avg-subarray-i [1,12,-5,-6,50,3] 4)))))

(test/run-test max-avg-subarray-i-test)
