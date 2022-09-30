(require '[clojure.set :refer :all])

(def people
  [{:person/name "Fred"}
   {:person/name "Fred"}
   {:person/name "Ethel"}
   {:person/name "Lucy"}])

;; similar to "group-by"
(clojure.set/index people [:person/name])
