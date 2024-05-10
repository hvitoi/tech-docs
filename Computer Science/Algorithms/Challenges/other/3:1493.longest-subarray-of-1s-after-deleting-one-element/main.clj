(require '[clojure.test :as test])

(defn remove-by-index
  [coll index]
  (concat (subvec coll 0 index)
          (subvec coll (inc index))))

(defn longest-subarray-of-ones
  [nums]
  (let [nums-variations (->> (range (count nums))
                             (map #(remove-by-index nums %)))]
    (->> nums-variations
         (map #(partition-by identity %))
         (map #(map count %))
         (map #(apply max %))
         (apply max))))

(test/deftest longest-subarray-of-ones-test
  (test/testing ""
    (test/is (= 3
                (longest-subarray-of-ones [1,1,0,1])))
    (test/is (= 5
                (longest-subarray-of-ones [0,1,1,1,0,1,1,0,1])))
    (test/is (= 2
                (longest-subarray-of-ones [1,1,1])))))

(test/run-test longest-subarray-of-ones-test)
