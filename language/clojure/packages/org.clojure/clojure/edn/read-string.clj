(require '[clojure.edn :as edn])

(edn/read-string
 "{#uuid \"f8d0d393-c8d0-47b2-9137-36dd78066793\" 
   {:name \"washdishes\"
    :status \"done\"},
   #uuid \"580cccf4-081f-4555-96db-7d1b1a716ee4\" 
   {:name \"washdishes\"
    :status \"done\"},
   #uuid \"9ca532c4-79c8-4490-97fd-211a1a6b8a11\" 
   {:name \"washdishes\"
    :status \"done\"}}")
