(require '[datomic.api :as d])

(def conn (d/connect "datomic:dev://localhost:4334/hello"))
(def db (d/db conn))

;; ---

; if nil, returns X

(or (d/q '[:find ?e .
           :where
           [?e :movie/title "Non-Existent"]]
         db) 0)
