(require '[clojure.test :as test])

(defn arr-chunk
  [arr max-chunk-size]
  (reduce
   (fn [chunked-arr el]
     (if (< (count (last chunked-arr)) max-chunk-size)
       (update chunked-arr
               (dec (count chunked-arr))
               #(conj % el))
       (conj chunked-arr [el])))
   [[]]
   arr))

(defn arr-chunk-native
  [arr max-chunk-size]
  (partition-all max-chunk-size arr))

(test/deftest chunk-test
  (test/testing "Divide array into chunks of 2"
    (test/is (= [[1 2]
                 [3 4]
                 [5 6]
                 [7 8]
                 [9 10]]
                (arr-chunk [1 2 3 4 5 6 7 8 9 10] 2))))

  (test/testing "Divide array into chunks of 1"
    (test/is (= [[1]
                 [2]
                 [3]]
                (arr-chunk [1 2 3] 1))))

  (test/testing "Divide array into chunks of 3"
    (test/is (= [[1 2 3]
                 [4 5]]
                (arr-chunk [1 2 3 4 5] 3))))

  (test/testing "Divide array into chunks of 5"
    (test/is (= [[1 2 3 4 5]
                 [6 7 8 9 10]
                 [11 12 13]]
                (arr-chunk [1 2 3 4 5 6 7 8 9 10 11 12 13] 5)))
    (test/is (= [[1 2 3 4 5]
                 [6 7 8 9 10]
                 [11 12 13]]
                (arr-chunk-native [1 2 3 4 5 6 7 8 9 10 11 12 13] 5))))

  (test/testing "Divide empty array into chunks"
    (test/is (= [[]]
                (arr-chunk [] 2)))))

(test/run-test chunk-test)
