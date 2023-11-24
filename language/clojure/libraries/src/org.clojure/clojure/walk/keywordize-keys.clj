(require '[clojure.walk :as walk])

(walk/keywordize-keys {"a" 1 "b" 2})

