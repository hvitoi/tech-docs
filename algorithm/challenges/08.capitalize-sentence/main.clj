(ns main
  (:require [clojure.test :as test]
            [clojure.string :as str]))

(defn capitalize-with-regex
  [sentence]
  (reduce
   (fn [capitalized-sentence char]
     (let [last-char-is-alphanumeric? (re-seq #"[A-z0-9]$" capitalized-sentence)]
       (if last-char-is-alphanumeric?
         (str capitalized-sentence char)
         (str capitalized-sentence (str/upper-case char)))))
   ""
   sentence))

(defn capitalize-with-split-and-capitalize
  [sentence]
  (->> (str/split sentence #" ")
       (map str/capitalize)
       (str/join " ")))

(test/deftest capitalize-test
  (test/testing "Capitalize a sentence"
    (test/is (= "My Name Is Henrique, Nice To Meet You! Ok?"
                (capitalize-with-regex "my name is henrique, nice to meet you! ok?")))
    (test/is (= "My Name Is Henrique, Nice To Meet You! Ok?"
                (capitalize-with-split-and-capitalize "my name is henrique, nice to meet you! ok?")))))

(test/run-test capitalize-test)
