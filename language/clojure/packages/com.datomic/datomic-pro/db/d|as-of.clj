(require '[datomic.api :as d])

(def conn (d/connect "datomic:dev://localhost:4334/hello"))
(def db (d/db conn))

;; ---

;; a snapshot of the database at a point in time
(d/as-of db #inst "2022-03-31")



;; find the instant where Star Wars was added
(d/q '[:find ?instant .
       :where
       [?e :movie/title "Star Wars" ?tx true]
       [?tx :db/txInstant ?instant]]
     db)
