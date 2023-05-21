(require '[clojure.string :as str])

(defn query-keywords
  [search-input]
  (->> (range 2 (+ (count search-input) 1))
       (map #(take % search-input))
       (map clojure.string/join)))

(defn suggestions-for-keyword
  [repository query-keyword]
  (->> repository
       (filter #(clojure.string/starts-with? % query-keyword))
       (take 3)))

(defn suggestions
  [repository search-input]
  (let [normalized-repository (map clojure.string/lower-case repository)
        normalized-search-input (clojure.string/lower-case search-input)]
    (->> (query-keywords normalized-search-input)
         (map #(suggestions-for-keyword normalized-repository %)))))

; --

(def repository ["mobile" "mouse" "moneypot" "monitor" "mousepad"])
(def search-input "mouse")
(suggestions repository search-input)
