(require '[clojure.string :as str])

(str/replace "abc" #"a" "b")

(str/replace "http://website.com/:id" ":id" "yay")