(require '[clojure.string :as string])

(string/lower-case "ABC")
(string/lower-case :ABC)
(string/lower-case nil) ; throws
