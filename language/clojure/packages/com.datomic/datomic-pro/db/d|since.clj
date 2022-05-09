(require '[datomic.api :as d])

(def conn (d/connect "datomic:dev://localhost:4334/hello"))
(def db (d/db conn))

;; ---

;; filter datoms created from a particular point in time
;; does not bring removed values (like history)
(def filtered-db (d/since db #inst "2022-03-31"))


;; usually "since" is used with a join (otherwise some ids would be missing)
;; search from 2 dbs at the same time
(d/q '[:find ?instant
       :in $ $filtered-db
       :where
       [$ ?movie :movie/title "Star Wars" ?tx] ; search in the whole db
       [$filtered-db ?tx :db/txInstant ?instant]] ; search in the filtered db
     db
     filtered-db)
