(require '[clojure.test :as test]
         '[clojure.string :as str])

(defn stairs
  [n]
  (->> (range n)
       (map inc)
       (map #(concat (repeat % "#")
                     (repeat (- n %) " ")))
       (map str/join)))

(defn stairs-recursive
  ([n] (stairs-recursive n 1))
  ([n i]
   (let [step (str/join (concat (repeat i "#")
                                (repeat (- n i) " ")))]
     (if (= n i)
       step
       (flatten [step (stairs-recursive n (inc i))])))))

(test/deftest stairs-test
  (test/testing "Build stairs with 3 steps"
    (test/is (= ["#  " "## " "###"]
                (stairs 3)))
    (test/is (= ["#  " "## " "###"]
                (stairs-recursive 3)))))

(test/run-test stairs-test)
