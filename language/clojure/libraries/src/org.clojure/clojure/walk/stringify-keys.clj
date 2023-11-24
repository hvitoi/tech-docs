(require '[clojure.walk :as walk])

(walk/stringify-keys {:a 1 :b 2})
