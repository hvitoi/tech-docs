(require '[clojure.test :as test])

(defprotocol Stackable
  (add-el [this element])
  (remove-el [this])
  (peek-el [this]))

(defrecord Queue [q]
  Stackable
  (add-el [_ el]
    (swap! q conj el))
  (remove-el [_]
    (swap! q next))
  (peek-el [_]
    (first @q)))

(defn new-queue []
  (->Queue (atom (lazy-seq))))

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

(test/deftest queue-test
  (test/testing "Test queue functions"
    (let [q (new-queue)]
      (test/is (= nil (peek-el q)))
      (test/is (= (seq []) (remove-el q)))
      (test/is (= (seq [:a]) (add-el q :a)))
      (test/is (= (seq [:b :a]) (add-el q :b)))
      (test/is (= :b (peek-el q)))
      (test/is (= (seq [:a]) (remove-el q)))
      (test/is (= (seq []) (remove-el q))))))

(test/run-test queue-test)

(test/deftest weave-test
  (test/testing ""
    (let [q1 [:a :b :c]
          q2 [1 2 3 4 5]]
      (test/is (= [:a 1 :b 2 :c 3 4 5] (weave q1 q2))))))

(test/run-test weave-test)
