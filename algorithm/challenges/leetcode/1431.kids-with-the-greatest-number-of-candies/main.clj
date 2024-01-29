(require '[clojure.test :as test])

(defn kids-with-most-candies
  [candies extra-candies]
  (let [max-candies (reduce
                     (fn [max el]
                       (if (> el max) el max))
                     0 candies)]
    (map #(>= (+ % extra-candies) max-candies)
         candies)))

(test/deftest kids-with-most-candies-test
  (test/testing "Calculate the array of kids with most candies"
    (test/is (= [true,true,true,false,true]
                (kids-with-most-candies [2,3,5,1,3] 3)))
    (test/is (= [true,false,false,false,false]
                (kids-with-most-candies [4,2,1,1,2] 1)))
    (test/is (= [true,false,true]
                (kids-with-most-candies [12,1,12] 10)))))

(test/run-test kids-with-most-candies-test)
