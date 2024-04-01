(require '[clojure.test :as test])

(defn weave
  [q1 q2]
  (loop [q1 q1
         q2 q2
         acc []]
    (let [el1 (first q1)
          el2 (first q2)
          acc (cond-> acc
                el1 (conj el1)
                el2 (conj el2))]
      (if (every? nil? [el1 el2])
        acc
        (recur (rest q1) (rest q2) acc)))))

(test/deftest weave-test
  (test/testing "Weave function"
    (let [q1 [:a :b :c]
          q2 [1 2 3 4 5]]
      (test/is (= [:a 1 :b 2 :c 3 4 5] (weave q1 q2))))))

(test/run-test weave-test)
