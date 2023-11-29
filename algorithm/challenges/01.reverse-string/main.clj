(require '[clojure.string :as str]
         '[clojure.test :as test])

(defn reserve-str-simple
  [string]
  (str/reverse string))

(defn reserve-str-with-reduce
  [string]
  (reduce
   (fn [acc char] (str char acc))
   ""
   string))

(defn reserve-str-with-for
  [string]
  (let [rev (atom [])]
    (doseq [char string]
      (swap! rev #(cons char %)))
    (str/join @rev)))

(test/deftest reverse-str-test
  (test/testing "Reverses a string"
    (test/is (= "edcba" (reserve-str-simple "abcde")))
    (test/is (= "edcba" (reserve-str-with-reduce "abcde")))
    (test/is (= "edcba" (reserve-str-with-for "abcde")))))

(test/run-test reverse-str-test)
