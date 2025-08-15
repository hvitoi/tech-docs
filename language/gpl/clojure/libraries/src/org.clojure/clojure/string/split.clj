(require '[clojure.string :as str])

(str/split "name,address,city,state,zip,email,phone" #",")
(str/split "abc" #"")
