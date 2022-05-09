(require '[datomic.api :as d])

(def conn (d/connect "datomic:dev://localhost:4334/hello"))
(def db (d/db conn))

;; ---

; count unique elements from the result
(d/q '[:find (count ?e)
       :where
       [?e :movie/title]]
     db)
