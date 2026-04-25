(require '[clojure.test :as test])

(defn max-consecutive-ones
  [nums k]
  (:max
   (reduce
    (fn [acc el]
      (let [new-acc
            (cond
              (and (zero? el) (not (pos-int? (:flips acc))))
              (-> acc
                  (assoc :current 1)
                  (assoc :flips (dec k)))

              (and (zero? el) (pos-int? (:flips acc)))
              (-> acc
                  (update :current inc)
                  (update :flips dec))

              (= 1 el)
              (-> acc
                  (update :current inc)))]
        (if (> (:current new-acc) (:max new-acc))
          (assoc new-acc :max (:current new-acc))
          new-acc)))
    {:current 0
     :flips k
     :max 0}
    nums)))

(test/deftest max-consecutive-ones-test
  (test/testing ""
    (test/is (= 6
                (max-consecutive-ones [1,1,1,0,0,0,1,1,1,1,0] 2)))
    (test/is (= 10
                (max-consecutive-ones [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1] 3)))
    (test/is (= 8
                (max-consecutive-ones [0, 0, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 0] 2)))))

(test/run-test max-consecutive-ones-test)
