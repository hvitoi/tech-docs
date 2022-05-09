(require '[datomic.api :as d])

(def conn (d/connect "datomic:dev://localhost:4334/hello"))
(def db (d/db conn))

;; ---

; sum unique results
(d/q '[:find (sum ?release-year)
       :where [?e :movie/release-year ?release-year]]
     db)
