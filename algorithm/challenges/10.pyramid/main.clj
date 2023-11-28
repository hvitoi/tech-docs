(ns main
  (:require [clojure.test :as test]
            [clojure.string :as str]))

(defn pyramid
  [n]
  (let [base-width (-> n (* 2) (- 1))]
    (->> (range n)
         (map inc)
         (map #(let [hashtags (-> % (* 2) (- 1))
                     whitespaces (- base-width hashtags)]
                 (concat (repeat (/ whitespaces 2) " ")
                         (repeat hashtags "#")
                         (repeat (/ whitespaces 2) " "))))
         (map str/join))))

(defn pyramid-recursive
  ([n] (pyramid-recursive n 1))
  ([n i]
   (let [base-width (-> n (* 2) (- 1))
         hashtags (-> i (* 2) (- 1))
         whitespaces (- base-width hashtags)
         stair (str/join (concat (repeat (/ whitespaces 2) " ")
                                 (repeat hashtags "#")
                                 (repeat (/ whitespaces 2) " ")))]
     (if (= n i)
       stair
       (flatten [stair (pyramid-recursive n (inc i))])))))

(test/deftest pyramid-test
  (test/testing "Build a pyramid with an amount of stairs"
    (test/is (= ["   #   " "  ###  " " ##### " "#######"]
                (pyramid 4)))
    (test/is (= ["   #   " "  ###  " " ##### " "#######"]
                (pyramid-recursive 4)))))

(test/run-test pyramid-test)
