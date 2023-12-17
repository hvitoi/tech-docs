(require '[clojure.test :as test])

(defprotocol IQueue
  (add-el [this element])
  (remove-el [this])
  (peek-el [this]))

(defrecord Queue [q]
  IQueue
  (add-el [_ el]
    (swap! q conj el))
  (remove-el [_]
    (swap! q next))
  (peek-el [_]
    (first @q)))

(defn new-queue []
  (->Queue (atom (lazy-seq))))

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
