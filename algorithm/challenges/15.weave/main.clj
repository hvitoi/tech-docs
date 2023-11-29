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
    (peek @q)))

(defn new-queue []
  (->Queue (atom (lazy-seq))))

(test/deftest foo-test
  (test/testing ""
    (let [q (new-queue)]
      (test/is (= nil (peek-el q)))
      (test/is (= (seq []) (remove-el q)))
      (test/is (= (seq [:a]) (add-el q :a)))
      (test/is (= (seq [:b :a]) (add-el q :b)))
      (test/is (= :b (peek-el q)))
      (test/is (= (seq [:a]) (remove-el q)))
      (test/is (= (seq []) (remove-el q)))
      ;
      )))

(test/run-test foo-test)
