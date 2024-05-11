(require '[clojure.test :as test])

(defn split-on-index
  [coll index]
  [(subvec coll 0 index)
   (subvec coll (inc index))])

(defn pivot-index
  [nums]
  (as-> (range (count nums)) $
    (map #(split-on-index nums %) $)
    (map #(= (apply + (first %))
             (apply + (second %))) $)
    (.indexOf $ true)))

(test/deftest pivot-index-test
  (test/testing ""
    (test/is (= 3
                (pivot-index [1,7,3,6,5,6])))
    (test/is (= -1
                (pivot-index [1,2,3])))
    (test/is (= 0
                (pivot-index [2,1,-1])))))

(test/run-test pivot-index-test)
