(ns solution
  (:require [clojure.string :as str]
            [clojure.test :as test]))

(defn query-keywords
  [search-input]
  (->> (range 2 (+ (count search-input) 1))
       (map #(take % search-input))
       (map str/join)))

(defn suggestions-for-keyword
  [repository query-keyword]
  (->> repository
       (filter #(str/starts-with? % query-keyword))
       (take 3)))

(defn suggestions
  [repository search-input]
  (let [normalized-repository (map str/lower-case repository)
        normalized-search-input (str/lower-case search-input)]
    (->> (query-keywords normalized-search-input)
         (map #(suggestions-for-keyword normalized-repository %)))))

; --

(test/deftest example
  (test/testing "Test example"
    (test/is (= [["mobile" "mouse" "moneypot"]
                 ["mouse" "mousepad"]
                 ["mouse" "mousepad"]
                 ["mouse" "mousepad"]]
                (suggestions
                 ["mobile" "mouse" "moneypot" "monitor" "mousepad"]
                 "mouse")))))
