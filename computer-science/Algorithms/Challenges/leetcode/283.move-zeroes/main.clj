(require '[clojure.test :as test])

(defn move-zeroes
  [nums]
  (let [zeroes (reduce (fn [sum num]
                         (if (zero? num)
                           (inc sum)
                           sum))
                       0 nums)]
    (concat
     (remove zero? nums)
     (repeat zeroes 0))))

(test/deftest move-zeroes-test
  (test/testing ""
    (test/is (= [1,3,12,0,0]
                (move-zeroes [0,1,0,3,12])))))

(test/run-test move-zeroes-test)
