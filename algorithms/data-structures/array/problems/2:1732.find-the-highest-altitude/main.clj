(require '[clojure.test :as test])

(defn highest-altitude
  [gain]
  (:max (reduce
         (fn [{:keys [current max]} gain]
           (let [current-altitude (+ current gain)]
             {:current current-altitude
              :max (if (> current-altitude max) current-altitude max)}))
         {:current 0 :max 0}
         gain)))

(test/deftest highest-altitude-test
  (test/testing ""
    (test/is (= 1
                (highest-altitude [-5,1,5,0,-7])))
    (test/is (= 0
                (highest-altitude [-4,-3,-2,-1,4,3,2])))))

(test/run-test highest-altitude-test)
